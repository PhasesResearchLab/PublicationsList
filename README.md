# How to Contribute?

To contribute to the list of publications, please follow the instructions below:

1\. Update the corresponding YAML file(s) in the 'publications' directory with your contributions at [PRL/PublicationsList's repository](https://github.com/PhasesResearchLab/PublicationsList).

> **Note:** The easiest and recommended method for editing file(s) is to do it directly from your browser using GitHub’s web-based editor. To do so, simply press the period key (.) on your keyboard when inside the PublicationList repo, and navigate to the YAML files using the 'Explorer' tab on the left sidebar menu. To commit your changes, use the 'Source Control' tab, write a short commit message, and click 'Commit & Push'.

> **Note:** When editing the YAML file(s), please be attentive to each entry's structure and order. Entries have specific fields that need to be filled accordingly or left 'null' if non-applicable (see examples below).

- **Articles** \| **In-Press**  \| **Pre-Prints**

    ```yaml
    - authors: 'Zi-Kui Liu, Nigel L. E. Hew, and Shun-Li Shang'
      title: Zentropy theory for accurate prediction of free energy, volume, and thermal
          expansion without fitting parameters
      metadata: 'Microstructures 4 (2024) 2024009.'
      DOI: https://dx.doi.org/10.20517/microstructures.2023.56
      arXiv: https://arxiv.org/abs/2310.06527
      URL: null
    ```

- **Book Chapters** \| **Patents**  \| **Webcasts** \| **Proceedings and Reports**

    ```yaml
    - metadata: 'Zi-Kui Liu, Advancing the Materials Genome, Proceedings Book of The 3rd 
        International Symposium on Steel Science (ISSS-2012) “Nanoscale inhomogeneity in 
        steels – Fundamentals and effects on microstructures and properties -“, page 1-10, 
        Edited by T. Furuhara, H. Numakura and K. Ushioda, 2012, The Iron and Steel 
        Institute of Japan, Tokyo, Japan2012-Liu-ZK-MGI-Japan'
      URL: 'http://www.phases.psu.edu/wp-content/uploads/2012-Liu-ZK-MGI-Japan.pdf'
    ```

> **Note:** Beware that article's old entries will exhibit an ID field, which is currently deprecated and can be omitted.

> **Note:** Entries are numbered sequentially in the reverse order they appeared in the document. For articles, to add a year separation between entries, add a 'bumpyear' entry between articles of different years.

- **Articles**

    ```yaml
    - bumpyear: true
    ```

2\. After updating the YAML file(s), commit the changes to the main branch, and you're good to go! The list will soon be automatically updated at [PRL Publications List's website](https://phasesresearchlab.github.io/PublicationsList/).