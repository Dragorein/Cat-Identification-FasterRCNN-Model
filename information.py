def Abyssnian(acc, image):
    infoData = ['Membutuhkan sedikit perawatan', 'Membutuhkan banyak perhatian', 'Cocok untuk hidup di dalam & luar ruangan']
    characteristicData = ["Sosial "," Aktif "," Setia "," Senang bersuara "," Penyayang"]
    data = {
        "predictionBreed" : 'Abisinia',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Bengal(acc, image):
    infoData = ['Pohon kucing itu sangat penting', 'Membutuhkan sedikit perawatan', 'Baik dengan anak-anak']
    characteristicData = ["Percaya diri "," Sosial "," Senang bersuara "," Energetik "," Ceria"]
    data = {
        "predictionBreed" : 'Bengal',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Birman(acc, image):
    infoData = ['Membutuhkan perawatan sedang', 'Sangat cocok untuk hidup di dalam ruangan', 'Baik dengan orang-orang']
    characteristicData = ["Sosial "," Setia "," Penyayang "," Diam "," Ceria "," Aktif"]
    data = {
        "predictionBreed" : 'Birman',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Bombay(acc, image):
    infoData = ['Membutuhkan sedikit perawatan', 'Cocok untuk hidup di dalam & luar ruangan', 'Seharusnya tidak dibiarkan sendiri']
    characteristicData = ["Pintar "," Penuh kasih sayang "," Sosial "," Tidak mudah marah "," Aktif"]
    data = {
        "predictionBreed" : 'Bombay',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def BritishShorthair(acc, image):
    infoData = ['Membutuhkan perawatan sedang', 'Cocok untuk hidup di dalam & luar ruangan', 'Perawatan minimum']
    characteristicData = ["Setia "," Penuh kasih sayang "," Diam "," Pintar"]
    data = {
        "predictionBreed" : 'British Shorthair',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def EgyptianMau(acc, image):
    infoData = ['Membutuhkan sedikit perawatan', 'Cocok untuk hidup di dalam & luar ruangan', 'Mudah terkejut']
    characteristicData = ["Lincah "," Aktif "," Sensitif "," Ceria "," Pintar"]
    data = {
        "predictionBreed" : 'Egyptian Mau',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def MaineCoon(acc, image):
    infoData = ['Membutuhkan perawatan sedang', 'Cocok untuk hidup di dalam & luar ruangan', 'Perawatan minimum']
    characteristicData = ["Tenang "," Diam "," Ramah"]
    data = {
        "predictionBreed" : 'Maine Coon',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Persian(acc, image):
    infoData = ['Paling cocok untuk rumah yang tenang', 'Membutuhkan banyak perawatan', 'Sangat cocok untuk hidup di dalam ruangan']
    characteristicData = ["Diam "," Tenang "," Sosial "," Penuh kasih sayang"]
    data = {
        "predictionBreed" : 'Persia',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Ragdoll(acc, image):
    infoData = ['Membutuhkan perawatan sedang', 'Sangat cocok untuk hidup di dalam ruangan', 'Sabar dengan anak-anak dan hewan lainnya']
    characteristicData = ["Tenang "," Sosial "," Ramah"]
    data = {
        "predictionBreed" : 'Ragdoll',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def RussianBlue(acc, image):
    infoData = ['Membutuhkan kandang luar ruangan', 'Membutuhkan sedikit perawatan', 'Sabar dengan anak-anak dan hewan lainnya']
    characteristicData = ["Sosial "," Pintar "," Ramah "," Ceria"]
    data = {
        "predictionBreed" : 'Russian',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Siamese(acc, image):
    infoData = ['Membutuhkan sedikit perawatan', 'Cocok untuk hidup di dalam & luar ruangan', 'Paling bahagia berpasangan']
    characteristicData = ["Penyayang "," Setia "," Ceria "," Senang bersuara "," Pintar "," Aktif"]
    data = {
        "predictionBreed" : 'Siam',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def Sphynx(acc, image):
    infoData = ['Membutuhkan banyak perawatan', 'Sabar dengan anak-anak dan hewan lainnya', 'Sangat cocok untuk hidup di dalam ruangan']
    characteristicData = ["Penuh kasih sayang "," Tidak mudah marah "," Lincah "," Pintar "," Sosial "," Diam"]
    data = {
        "predictionBreed" : 'Sphynx',
        "predictionAccuracy" : acc,
        "imageBase64" : image.decode("utf-8"),
        "information" : infoData,
        "characteristic" : characteristicData
    }
    return data

def none(image):
    data = {
        "predictionBreed" : 'Kucing tidak terdeteksi',
        "predictionAccuracy" : 0,
        "imageBase64" : image.decode("utf-8"),
        "information" : ["Kucing tidak terdeteksi"],
        "characteristic" : ['Kucing tidak terdeteksi']
    }
    return data

