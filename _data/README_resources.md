# Resources Management

The Resources page (`/resources/`) is automatically generated from the data in `_data/resources.yml`. 

## How to Add New Resources

### Adding a Protocol

To add a new protocol, edit `_data/resources.yml` and add a new entry under the `protocols:` section:

```yaml
protocols:
  - title: "Your Protocol Name"
    description: "A detailed description of what this protocol does and why it's useful."
    download_url: "https://example.com/your-protocol.pdf"
    download_text: "Download Protocol"
```

### Adding Software/Tools

To add software or computational tools, add entries under the `software:` section:

```yaml
software:
  - title: "Your Software Name"
    description: "Description of what the software does and its main features."
    download_url: "https://github.com/yourusername/repo"
    download_text: "View on GitHub"
```

### Adding Datasets

To add datasets, add entries under the `datasets:` section:

```yaml
datasets:
  - title: "Your Dataset Name"
    description: "Description of the dataset, what it contains, and how it was generated."
    download_url: "https://zenodo.org/record/your-dataset"
    download_text: "Access Dataset"
```

## Required Fields

Each resource entry must have these four fields:
- `title`: The name of the resource
- `description`: A detailed description
- `download_url`: The URL where users can access/download the resource
- `download_text`: The text that appears on the download button

## Notes

- The page will automatically show placeholder text ("will be added here as they become available") for empty sections
- Each resource appears as an expandable accordion item
- All resources open in a new tab/window when clicked
- All resource links open in a new tab/window when clicked
- The page regenerates automatically when you save changes to `resources.yml` 