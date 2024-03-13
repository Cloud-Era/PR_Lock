name: Deploy Site

on:
  push:
    branches:
      - master
    paths:
      - 'docs/**'
      - '*.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      
      - name: Set up Python 3.7
        uses: actions/setup-python@v1
        with:
          python-version: 3.7
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip setuptools
          python -m pip install -r requirements.txt
      
      - name: Deploy Files
        run: |
          git config --local user.name "${{ secrets.GH_USER }}"
          git config --local user.email "${{ secrets.GH_MAIL }}"
          git remote add gh-token "https://${{ secrets.GH_TOKEN }}@github.com/${{ git
