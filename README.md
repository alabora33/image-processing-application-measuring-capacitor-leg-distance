# image-processing-application-measuring-capacitor-leg-distance


Bu komut dosyası, bir görüntüdeki kapasitör bacakları arasındaki mesafeyi hesaplamak için tasarlanmıştır. Bacaklar, y ekseninde 480 – 680 piksel arasında 1600x200 piksel İlgi Alanı (ROI) olarak tanımlanır. Mesafe, kapasitör ayaklarının en alt noktasının 20 piksel üzerinde ölçülür. Komut dosyası ayrıca algoritmanın toplam işlem süresini de yazdırır.

Betik gerekli kütüphaneleri içe aktararak başlar: görüntü işleme için OpenCV (cv2), sayısal işlemler için numpy ve işlem süresini ölçmek için time.

'DistanceCalculation' adında bir sınıf tanımlanmış olup, bu sınıfta görüntüyü işlemek, kapasitör ayakları üzerindeki noktaları bulmak ve bu noktalar arasındaki mesafeyi hesaplamak için yöntemler bulunmaktadır.

__init__` yönteminde görüntü okunur ve ROI sınırları tanımlanır.

"process_image" yöntemi ROI'yi çıkarır, ROI'ye çift taraflı bir filtre uygular ve Canny kenar tespiti yapar, ardından sonuç görüntüsündeki konturları bulur. Kondansatör ayakları üzerindeki noktaları bulur ve aralarındaki mesafeyi hesaplar. Noktalar bulunursa noktalar, kapasitör ayaklarının en alt noktasının 20 piksel yukarısına ayarlanır. Daha sonra her bir bacağın orta noktasını hesaplar, orta noktalar arasına bir çizgi çizer ve mesafeyi görüntü üzerinde çizer. İşlenen görüntüyü görüntüler, kaydeder ve mesafeyi döndürür. Noktalar bulunamazsa bir mesaj yazdırılır ve Hiçbiri döndürülür.

'Find_point' yöntemi, daha büyük konturların bacaklar olma ihtimalinin yüksek olduğunu varsayarak konturları alanlarına göre sıralar. Yalnızca en büyük iki konturu korur. Her bir kontur için, konturun momentini hesaplayarak merkezin x,y koordinatlarını hesaplar. ROI dengelemesi için noktalar ayarlanır ve döndürülür.

'Find_distance' yöntemi, Öklid mesafe formülünü kullanarak iki nokta arasındaki mesafeyi hesaplar.

Komut dosyasının ana bölümünde görüntünün yolunu içeren 'DistanceCalculation' sınıfının bir örneği oluşturulur. 'process_image' yöntemi çağrılır ve mesafe Yok değilse yazdırılır. Algoritmanın toplam işlem süresi de yazdırılır.

![processed_image](https://github.com/alabora33/image-processing-application-measuring-capacitor-leg-distance/assets/41023507/18457be6-9fbf-4433-ae2a-4c2ea87ce501)
