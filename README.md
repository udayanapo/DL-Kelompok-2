# DL-Kelompok-5
Anggota kelompok :
  1. Komang Kurnia Suestiana (1805551121) -- Git username : komangkurnia
  2. I Putu Udayana Setya Ananta (1805551151) -- Git username : udayanapo
  3. Nathania Novenrodumetasa (1905551083)
  4. Angga Destia Faturrahman (1905551100)
  
**Deskripsi Aplikasi**

&nbsp; Klasifikasi Genre Musik merupakan aplikasi berbasis web untuk mengklasifikasikan genre dari suatu input audio. Website akan menerima inputan musik dengan format audio .wav, .mp3, lalu akan ditampilkan dalam user interface genre musik tersebut akan di klasifikasikan ke dalam sebuah genre dengan presentase keyakinan dari hasil model deep learning. Model deep learning yang dipakai menggunakan GRU dan menggunakan bahasa pemrograman Python.

**Arsitektur Aplikasi**

&nbsp; Didalam website, user akan memasukan input data berupa format audio seperti .wav, .mp3. Setelah itu, untuk mengklasifikasikan sebuah musik, user akan menekan tombol check genre, maka akan muncul output sebuah teks berupa genre musik dari musik tersebut serta persentase keyakinan genre tersebut berdasarkan hasil dari model deep learning yang sudah dibuah.

**Penjelasan Detail Dataset**

&nbsp; Dataset diambil dari KAGGLE https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification yang berisikan 10 genre musik yang masing- masing berisikan 100 lagu berdurasi 30 detik. untuk menggunakan dataset audio, diperlukan preprosesing audio kedalam bentuk MFCC yang sudah ada dalam file model GRU.

**Penjelasan Algoritma Deep Learning**

&nbsp; Audio merupakan data sequential, maka dari itu digunakanlah RNN. RNN cocok untuk digunakan dalam menyelesaikan problem yang mempunyai data berbentuk sekuensial. Pengembangan RNN pun terus berkembang pesat, dan banyak penelitian yang sudah menghasilkan Artificial Intelligence (AI) berakurasi tinggi dengan menggunakan RNN, mulai dari sentiment analysis, speech recognition, hingga video captioning. Perkembangan RNN pun disertai dengan modifikasi dari RNN tradisional menjadi RNN yang lebih adaptif, seperti LSTM. Salah satu varian LSTM yaitu GRU. GRU mempunyai komputasi yang lebih sederhana dari LSTM, namun mempunyai akurasi yang setara dan masih cukup efektif untuk menghindari permasalahan vanishing gradient.

**Penjelasan Proses training dan testing**

&nbsp; Dalam proses training menggunakan 30 epochs, dengan 800 data training, mendapatkan hasil loss = 0,1300 accuracy = 0,9551 validasi loss = 0,8051 validasi accuracy = 0,7881 

**Analisis terhadap model dan evaluasi**

&nbsp; Model Gru mengalahkan Model LSTM dengan accuracy yang hampir mendekati. Untuk mendapatkan hasil yang lebih bagus, mungkin bisa menambah jumlah epochs yang banyak. dalam model GRU ini hanya menggunakan 30 epochs untuk mempersingkat waktu training. Dataset Genre bisa lebih diperbanyak karena dalam dunia musik, terdapat banyak sekali genre, dan di model ini hanya dilimitasi hanya 10 genre saja.

**Cara Menjalankan Aplikasi**



