# DL-Kelompok-5
Anggota kelompok :
  1. Komang Kurnia Suestiana (1805551121) -- Git username : komangkurnia
  2. I Putu Udayana Setya Ananta (1805551151) -- Git username : udayanapo
  3. Nathania Novenrodumetasa (1905551083)
  4. Angga Destia Faturrahman (1905551100)
  
**Deskripsi Aplikasi**

  Deep learning adalah metode dalam kecerdasan buatan yang mengajarkan komputer untuk memproses data dengan cara yang terinspirasi otak manusia. Model deep learning dapat mengenali pola kompleks dalam gambar, teks, suara, dan data lain untuk menghasilkan wawasan dan prediksi yang akurat. Pada laporan ini membahas tentang model deep learning untuk mengklasifikasikan input music ke dalam output genre musik pada aplikasi berbasis website. Website akan menerima inputan musik dengan format audio .wav, .mp3, lalu akan ditampilkan dalam user interface genre musik tersebut akan di klasifikasikan ke dalam sebuah genre dengan presentase keyakinan dari hasil model deep learning. Model deep learning yang dipakai menggunakan GRU dan menggunakan bahasa pemrograman Python.
Dalam dunia musik, banyak orang yang masih bingung cara dengan membedakan musik berdasarkan genrenya. Oleh karena itu, dibuatlah Klasifikasi Genre Musik untuk membantu mengklasifikasikan musik sesuai dengan genrenya tanpa harus mendengarkan semua durasi dari sebuah lagu dengan tujuan 
1. Pengguna bisa mempelajari ciri-ciri dari setiap genre musik
2. Untuk mempermudah memilah musik berdasarkan genre musik
3. Mengurangi beban waktu dengan automatisasi 

**Arsitektur Aplikasi**

  Didalam website, user akan memasukan input data berupa format audio seperti .wav, .mp3. Setelah itu, untuk mengkasifikasikan sebuah musik, user akan menekan tombol check genre, maka akan muncul output sebuah teks berupa genre musik dari musik tersebut serta persentase keyakinan genre tersebut berdasarkan hasil dari model deep learning yang sudah dibuah.

**Penjelasan Detail Dataset**

  Dataset diambil dari KAGGLE https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification yang berisikan 10 genre musik yang masing- masing berisikan 100 lagu berdurasi 30 detik. untuk menggunakan dataset audio, diperlukan preprosesing audio kedalam bentuk MFCC 
**
Penjelasan Algoritma Deep Learning**

  Audio merupakan data sequential, maka dari itu digunakanlah RNN. RNN cocok untuk digunakan dalam menyelesaikan problem yang mempunyai data berbentuk sekuensial. Pengembangan RNN pun terus berkembang pesat, dan banyak penelitian yang sudah menghasilkan Artificial Intelligence (AI) berakurasi tinggi dengan menggunakan RNN, mulai dari sentiment analysis, speech recognition, hingga video captioning. Perkembangan RNN pun disertai dengan modifikasi dari RNN tradisional menjadi RNN yang lebih adaptif, seperti LSTM. Salah satu varian LSTM yaitu GRU. GRU mempunyai komputasi yang lebih sederhana dari LSTM, namun mempunyai akurasi yang setara dan masih cukup efektif untuk menghindari permasalahan vanishing gradient.

**Penjelasan Proses training dan testing**

  Dalam proses training menggunakan 30 epochs, dengan 800 data training, mendapatkan hasil loss = 0,1300 accuracy = 0,9551 validasi loss = 0,8051 validasi accuracy = 0,7881 d
