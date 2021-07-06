# Code linting

Purpose of this section is to demonstrate code linting

Note: install pylance extension and set the following for workspace settings. For convenience, this is already in the repo: `.vscode/settings.json`.

```json
{
    "python.linting.enabled": true,
    "python.analysis.typeCheckingMode": "basic"
}
```

* Errors are shown with red squiggles: `red-error-squiggles.py`
* Warnings are shown with yellow squiggles: `red-error-squiggles.py`
* Other warnings are shown with dimmed code: `dimmed-code-warnings.py`
* Source files with errors/warnings are highlighted in red/yellow in the file browser
* Errors and warnings are shown in the `PROBLEMS` tab in the vscode terminal window


  * Errors vs warnings vs... whatever the green one is
  * Introduce errors for malformed code
  * Introduce highlights for used/unused/unreachable code
* Introduce auto text alignment (when dealing with recognized file types)