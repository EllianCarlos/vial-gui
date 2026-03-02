### vial-gui

> **⚠️ Fork Notice:** This is an unofficial fork of [vial-kb/vial-gui](https://github.com/vial-kb/vial-gui) with a fix for running on macOS 15+ with Apple Silicon. The original release (v0.7.5) crashes due to an `IOHIDManager` threading issue under Rosetta 2. This fork replaces the `fbs_runtime` dependency with a minimal stub so it can run from source with modern Python (3.11+). For the official project, visit the upstream repo.

# Docs and getting started

### Please visit [get.vial.today](https://get.vial.today/) to get started with Vial

Vial is an open-source cross-platform (Windows, Linux and Mac) GUI and a QMK fork for configuring your keyboard in real time.


![](https://get.vial.today/img/vial-win-1.png)


---


#### Releases

Visit https://get.vial.today/ to download a binary release of Vial.

#### Development

Python 3.6 is recommended (3.6 is the latest version that is officially supported by `fbs`).

Install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To launch the application afterwards:

```
source venv/bin/activate
fbs run
```
