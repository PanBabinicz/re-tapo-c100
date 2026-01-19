# Tapo C100 reverse engineering

## How to obtain passwd and shadow files?

> After extracting the firmware with `binwalk`, search the extracted
> filesystem for password entries by looking for lines that start with
> `root:`.

```console
~ grep -ar "^root:" <path-to-extraction-dir>
```
