name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Build with Buildozer
        uses: ArtemSerebrenninkov/buildozer-action@v1
        with:
          buildozer_version: stable
          python_version: 3.9

      - name: Upload APK
        uses: actions/upload-artifact@v2
        with:
          name: DuckBot-Installer
          path: bin/*.apk
          
        
