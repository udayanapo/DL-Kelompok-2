# Back End

## Instalasi

* Lakukan Cloning terhadap repository ini
* Masuk ke direktori folder, lalu buat virtual environment dengan mengetikkan perintah berikut ini
  ``` bash 
  python -m venv genre-venv
  ``` 
    ```genre-venv``` merupakan nama dari virtual environment yang akan dibuat
* Masuk ke virtual environment dengan mengetikkan perintah berikut
  ``` bash
  genre-venv\Scripts\activate 
  ```
* Lakukan instalasi library yang dibutuhkan dengan mengetikkan perintah berikut
  ``` bash
  pip install -r requirements.txt 
  ```
* Untuk menjalankan flask dapat menggunakan perintah berikut
  ``` bash
  flask -app server run
  ```
  
 ## End Point API
  * Prediksi menggunakan Model LSTM
    - End Poin
      ```bash 
      /predict/lstm
      ```
    - Method ``` POST ```
    - Output
      ``` bash
      {
        "genre": "Classical"
      }
      ```
      
  * Prediksi menggunakan Model GRU
    - End Poin
      ```bash 
      /predict/gru
      ```
    - Method ``` POST ```
    - Output
      ``` bash
      {
        "genre": "Classical"
      }
      ```
