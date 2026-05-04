import requests
from bs4 import BeautifulSoup
import time

def scrape_acibadem_general(url):
    # Üniversite sitesine 'ben bir tarayıcıyım' diyoruz
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Hocanın istediği nezaket kuralı: İsteği atmadan önce bekle
    time.sleep(2)
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Gereksiz kod parçalarını temizliyoruz
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Sadece metni alıyoruz
            text = soup.get_text(separator=' ', strip=True)
            return text
        else:
            print(f"Hata kodu: {response.status_code} - Sayfa bulunamadı veya erişim engellendi.")
            return None
    except Exception as e:
        print(f"Bağlantı sırasında bir hata oluştu: {e}")
        return None

if __name__ == "__main__":
    # 404 almamak için ana sayfadan başlıyoruz
    target_url = "https://www.acibadem.edu.tr/" 
    print(f"{target_url} adresi taranıyor, lütfen bekleyin...")
    
    data = scrape_acibadem_general(target_url)
    
    if data:
        print("\n--- Veri başarıyla çekildi kanka! ---")
        # İlk 500 karakteri ekrana basıp kontrol edelim
        print(data[:500])
    else:
        print("\nMaalesef veri çekilemedi. Linki veya internet bağlantısını kontrol etmelisin.")