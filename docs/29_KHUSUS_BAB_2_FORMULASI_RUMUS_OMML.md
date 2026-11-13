# II. METODE PENELITIAN

## *D. Validasi Tiga Metrik dan Formulasi Algoritma FP-Growth*

Kaidah asosiasi yang terbentuk dari penambangan pohon frekuensi pola FP-Tree dievaluasi dan divalidasi secara kuantitatif menggunakan Standar Validasi Tiga Metrik (*Tri-Metric Validation*) [2], [4]. Prosedur validasi ini bertujuan memverifikasi derajat keandalan matematis serta mengeliminasi kaidah semu (*spurious rules*) yang berpotensi timbul akibat dominasi varian transaksi tertentu. Evaluasi mencakup tiga pilar metrik kuantitatif: *Support* (tingkat dukungan), *Confidence* (tingkat kepastian bersyarat), dan *Lift Ratio* (rasio angkat dependensi).

Tingkat dukungan (*Support*) merefleksikan probabilitas gabungan $P(X \cap Y)$ dari kemunculan simultan itemset anteseden ($X$) dan itemset konsekuen ($Y$) terhadap seluruh populasi transaksi yang tersimpan dalam basis data ($|D|$). Formulasi matematis tingkat dukungan disajikan pada Persamaan (1):

$$\text{Support}(X \Rightarrow Y) = P(X \cap Y) = \frac{\sigma(X \cup Y)}{|D|} \tag{1}$$

di mana $X$ melambangkan itemset anteseden (kondisi prasyarat), $Y$ melambangkan itemset konsekuen (hasil prediksi), $\sigma(X \cup Y)$ menyatakan frekuensi kemunculan absolut faktur penjualan yang memuat atribut $X$ dan $Y$ secara bersamaan, dan $|D|$ adalah total populasi data transaksi yang diteliti secara sensus ($|D| = 3.113$ transaksi).

Tingkat kepastian bersyarat (*Confidence*) mengukur derajat keandalan atau probabilitas bersyarat $P(Y \mid X)$, yaitu seberapa sering konsekuen $Y$ muncul dalam transaksi dengan syarat bahwa anteseden $X$ telah terjadi. Formulasi matematis *Confidence* disajikan pada Persamaan (2):

$$\text{Confidence}(X \Rightarrow Y) = P(Y \mid X) = \frac{\text{Support}(X \cup Y)}{\text{Support}(X)} = \frac{\sigma(X \cup Y)}{\sigma(X)} \tag{2}$$

di mana $\text{Support}(X \cup Y)$ merupakan tingkat dukungan gabungan itemset $X$ dan $Y$, sedangkan $\text{Support}(X)$ atau $\sigma(X)$ adalah frekuensi kemunculan anteseden $X$ secara mandiri dalam basis data penjualan.

Meskipun suatu aturan memiliki nilai *Confidence* yang tinggi, kaidah tersebut dapat bersifat bias dan menyesatkan apabila konsekuen $Y$ pada dasarnya sudah memiliki popularitas penjualan yang sangat masif (*unconditional popularity*). Oleh karena itu, kekuatan dependensi murni diuji menggunakan *Lift Ratio*, yang mengukur rasio perbandingan antara probabilitas bersama aktual terhadap probabilitas ekspektasi acak dengan asumsi kedua item saling bebas secara statistik (*statistically independent*). Formulasi *Lift Ratio* dinyatakan pada Persamaan (3):

$$\text{Lift}(X \Rightarrow Y) = \frac{\text{Confidence}(X \Rightarrow Y)}{\text{Support}(Y)} = \frac{P(X \cap Y)}{P(X) \times P(Y)} \tag{3}$$

di mana $P(X \cap Y)$ merupakan probabilitas gabungan aktual transaksi, sedangkan $P(X) \times P(Y)$ mencerminkan probabilitas teoritis kemunculan bersama jika pembelian $X$ dan $Y$ tidak memiliki hubungan kausalitas apa pun.

Berdasarkan nilai *Lift Ratio*, kaidah asosiasi diklasifikasikan ke dalam tiga tingkatan evaluasi ilmiah sebagai landasan penyaringan kelayakan implementasi bisnis:

1. **Lift Ratio > 1,0** : Menunjukkan adanya interdependensi positif murni (*positive correlation*). Kemunculan anteseden $X$ secara nyata meningkatkan probabilitas terjadinya konsekuen $Y$ dibandingkan ekspektasi acak. Kaidah ini dinyatakan valid, kokoh secara statistik, dan bernilai strategis tinggi untuk diimplementasikan.
2. **Lift Ratio = 1,0** : Menunjukkan bahwa kemunculan anteseden $X$ dan konsekuen $Y$ bersifat saling bebas (*statistically independent*). Kehadiran $X$ sama sekali tidak mempengaruhi peluang terjadinya $Y$, sehingga kemunculan bersama hanyalah ko-insidensi kebetulan yang tidak memiliki nilai analitis (wajib dieliminasi).
3. **Lift Ratio < 1,0** : Menunjukkan adanya hubungan asosiasi negatif atau efek substitusi (*mutual exclusivity*). Keberadaan anteseden $X$ secara sistematis justru menurunkan peluang kemunculan konsekuen $Y$, sehingga kaidah dikategorikan bertentangan dengan logika pasar dan wajib dieliminasi secara otomatis [2], [4].

Seluruh kaidah asosiasi yang lolos pengujian ambang batas Minimum Support $\ge 1,0\%$, Minimum Confidence $\ge 60,0\%$, dan Lift Ratio $> 1,0$ selanjutnya ditabulasi dan disintesis ke dalam tiga pilar rekomendasi preskriptif operasional dealer: (1) Panduan Penawaran Penjualan Cerdas bagi pramuniaga (*Smart Sales Script*) berbasis afinitas lintas-atribut, (2) Alokasi Persediaan Regional Varian dan Warna (*Regional Inventory Allocation*) guna mengeliminasi kelangkaan stok (*stockout*) dan penumpukan barang lambat laku (*dead stock*), serta (3) Program Promosi Pembiayaan Terpadu (*Joint Multifinance Bundling Program*) bersama lembaga leasing rekanan (BAF, Adira, OTO) [4].
