# Code linting

A linter is used to find errors, warnings, or stylistic problems in source code before compilation or runtime. When a linter is integrated with an IDE (such as VS Code), this is all done in real time as you type, and the results of linting are shown in a variety of ways.

The term "lint" comes from software used by Bell Labs starting in 1978 that found small defects in code, just like a dryer finds small pieces of lint in clothes ([see wikipedia article](https://en.wikipedia.org/wiki/Lint_(software))).

![dryer lint](https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Dryer_lint.jpg/800px-Dryer_lint.jpg)
<!-- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Dryer_lint.jpg/800px-Dryer_lint.jpg" alt="dryer lint" style="width:200px;border:solid 1px gray" /> -->
<!-- While the native Markdown link inclusion doesn't include the width styling, it looks like Github wasn't honoring that anyway. -->

## Greyed out (dimmed) code warnings

With the proper configuration, VS Code will warn about unused or unreachable code by greying out (or dimming) Python code in the following cases:

* Unused imports
* Unused variables
* Unreachable code
* Unused functions

![Dimmed code warnings](./assets/dimmed-code-warnings.png)
<!-- <img src="./assets/dimmed-code-warnings.png" alt="dimmed-code-warnings" style="max-width:600px;border:solid 1px gray" /> -->

Mouse hover over a greyed out word to get info about the warning:

![Additional info from dimmed code warnings](./assets/dimmed-code-warnings-b.png)
<!-- <img src="./assets/dimmed-code-warnings-b.png" alt="dimmed-code-warnings-b" style="max-width:600px;border:solid 1px gray" /> -->

See [dimmed-code-warnings.py](./assets/dimmed-code-warnings.py)

## Error squiggles

Errors in Python code are indicated with red squiggles in the following cases:

* Import not found
* Syntax error
* Incorrect argument type (when using static type hints)
* Mismatched parentheses or quotes
* etc.

![Red error squiggles](./assets/red-error-squiggles.png)
<!-- <img src="./assets/red-error-squiggles.png" alt="red-error-squiggles" style="max-width:600px;border:solid 1px gray" /> -->

See [red-error-squiggles.py](./assets/red-error-squiggles.py)

Warnings are indicated with yellow squiggles.
![Yellow warning squiggles](./assets/yellow-warning-squiggles.png)
<!-- <img src="./assets/yellow-warning-squiggles.png" alt="yellow-warning-squiggles" style="max-width:600px;border:solid 1px gray" /> -->

See [yellow-warning-squiggles.py](./assets/yellow-warning-squiggles.py)

Other color squiggles can indicate other problems such as unrecommended code constructs or styles.

## File explorer - highlighting of errors/warnings

Open files with errors or warnings are highlighted in red or yellow in the file explorer.

![File explorer](./assets/file-explorer.png)
<!-- <img src="./assets/file-explorer.png" alt="file-explorer" style="max-width:600px;border:solid 1px gray" /> -->

## 'PROBLEMS' tab

Errors and warnings for open files are also listed in the PROBLEMS tab in the terminal area.

![Problems tab](./assets/problems-tab.png)
<!-- <img src="./assets/problems-tab.png" alt="problems-tab" style="max-width:600px;border:solid 1px gray" /> -->
