from click import command, option, Path
import bibtexparser
from typing import Dict, Union, List
import json
from sys import exit
from pdb import set_trace


def format_author(author_string: str) -> List[Dict[str, str]]:
    author_list = []
    authors = author_string.split(" and ")

    for author in authors:
        author_entry = {
            "family": author.split(", ")[0],
            "given": "".join(author.split(", ")[1:])
        }
        author_list.append(author_entry)

    return author_list


def format_date(year: str) -> Dict[str, List[List[str]]]:
    return {
        "date-parts": [
            [
                year
            ]
        ]
    }


def extract_year(entry: Dict) -> int:
    return int(entry["issued"]["date-parts"][0][0])


@command()
@option("--input", "-i", type=Path(exists=True), default=None, show_default=True, help="Bibtex file path")
@option("--output", "-o", type=Path(), default=None, show_default=True, help="Path to output JSON file")
@option("--sort", "-s", type=bool, is_flag=True, default=False, help="Flag to sort JSON entries by date")
@option("--reverse", "-r", type=bool, is_flag=True, default=False, help="Reverses date sorting. Only used if --sort or -s is used.")
def main(input, output, sort, reverse) -> None:
    with open(input, "r") as f:
        library = bibtexparser.load(f)

    new_entries: List[Dict[str, Union[str, List[Dict[str, str]]]]] = []
    for entry in library.entries:
        try:
            new_entry = {
                "id": entry["ID"],
                "type": entry["ENTRYTYPE"],
                "title": entry["title"],
                "container-title": entry["journal"] if "journal" in entry else "",
                "page": "",
                "volume": entry["volume"] if "volume" in entry else "",
                "issue": entry["number"] if "number" in entry else "",
                "source": entry["publisher"] if "publisher" in entry else "",
                "abstract": entry["abstract"] if "abstract" in entry else "",
                "DOI": entry["doi"] if "doi" in entry else "",
                "author": format_author(entry["author"]) if "author" in entry else "",
                "issued": format_date(entry["year"]) if "year" in entry else ""
            }
        except KeyError as e:
            print(e)
            print(entry)
            exit(1)

        new_entries.append(new_entry)

    with open(output, "w") as fout:
        if sort:
            new_entries_dict = {idx: entry for idx, entry in enumerate(new_entries)}
            new_entries_dict_sorted = dict(sorted(new_entries_dict.items(),
                                                  key=lambda x: extract_year(x[1]),
                                                  reverse=reverse))
            entries_to_write = list(new_entries_dict_sorted.values())
        else:
            entries_to_write = new_entries

        json.dump(entries_to_write,
                  fout,
                  sort_keys=True,
                  indent=4,
                  separators=(',', ': '))


if __name__ == "__main__":
    main()
