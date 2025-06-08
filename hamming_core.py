import random

class HammingCore:
    def __init__(self):
        # Temel değişkenler
        self.current_code = None
        self.current_size = 8

    def set_size(self, size):
        # Veri boyutunu ayarla
        self.current_size = size
        self.current_code = None

    def generate_random_data(self, size):
        # Rastgele binary veri oluştur
        return ''.join([str(random.randint(0, 1)) for _ in range(size)])

    def encode_and_store(self, data):
        # Veriyi kodla ve hafızaya kaydet
        if not data or not all(bit in '01' for bit in data) or len(data) != self.current_size:
            return False, "Invalid data"

        # Hamming kodlaması
        encoded = self.encode_hamming_secded(data)

        # Hafızaya kaydet
        self.current_code = {
            'original': data,
            'encoded': encoded,
            'current': encoded
        }

        return True, "Data encoded successfully"

    def introduce_single_error(self):
        # Tek bit hata oluştur
        if not self.current_code:
            return False, "No data to modify"

        current_data = list(self.current_code['current'])
        error_pos = random.randint(0, len(current_data) - 1)
        current_data[error_pos] = '1' if current_data[error_pos] == '0' else '0'
        self.current_code['current'] = ''.join(current_data)

        return True, f"Single error introduced at position {error_pos}"

    def introduce_double_error(self):
        # Çift bit hata oluştur
        if not self.current_code:
            return False, "No data to modify"

        current_data = list(self.current_code['current'])
        error_positions = random.sample(range(len(current_data)), 2)
        
        for pos in error_positions:
            current_data[pos] = '1' if current_data[pos] == '0' else '0'
        
        self.current_code['current'] = ''.join(current_data)

        return True, f"Double errors introduced at positions {error_positions}"

    def detect_and_correct(self):
        # Hataları tespit et ve düzelt
        if not self.current_code:
            return False, "No data to analyze"

        # Kodu analiz et
        decoded, status = self.decode_hamming_secded(self.current_code['current'])

        # Sendrom hesapla
        syndrome = 0
        received = self.current_code['current']
        for i in range(len(received)):
            if self.is_power_of_2(i) and i != 0:
                parity = 0
                for j in range(i, len(received), 2 * i):
                    for k in range(j, min(j + i, len(received))):
                        parity ^= int(received[k])
                if parity != 0:
                    syndrome += i

        result = {
            'status': status,
            'syndrome': syndrome,
            'current_data': self.current_code['current'],
            'original_data': self.current_code['encoded']
        }

        if "Single error detected" in status:
            error_pos = syndrome
            corrected = self.correct_single_error(self.current_code['current'], error_pos)
            corrected_decoded, _ = self.decode_hamming_secded(corrected)
            
            result.update({
                'error_position': error_pos,
                'corrected_data': corrected,
                'corrected_decoded': corrected_decoded
            })

        return True, result

    def apply_correction(self):
        # Düzeltmeyi uygula
        if not self.current_code:
            return False, "No data to correct"

        decoded, status = self.decode_hamming_secded(self.current_code['current'])
        if "Single error detected" in status:
            syndrome = 0
            received = self.current_code['current']
            for i in range(len(received)):
                if self.is_power_of_2(i) and i != 0:
                    parity = 0
                    for j in range(i, len(received), 2 * i):
                        for k in range(j, min(j + i, len(received))):
                            parity ^= int(received[k])
                    if parity != 0:
                        syndrome += i

            corrected = self.correct_single_error(self.current_code['current'], syndrome)
            self.current_code['current'] = corrected
            return True, "Correction applied successfully"
        
        return False, "No correction needed or possible"

    def encode_hamming_secded(self, data):
        # Hamming SEC-DED kodlaması
        data_bits = len(data)
        parity_bits = self.calculate_parity_bits(data_bits)
        total_bits = data_bits + parity_bits

        # Kod kelimesi dizisi oluştur
        codeword = ['0'] * total_bits

        # Veri bitlerini yerleştir
        data_index = 0
        for i in range(1, total_bits):
            if not self.is_power_of_2(i) and i != 0:
                if data_index < len(data):
                    codeword[i] = data[data_index]
                    data_index += 1

        # Parite bitlerini hesapla
        for i in range(total_bits):
            if self.is_power_of_2(i) and i != 0:
                parity = 0
                for j in range(i, total_bits, 2 * i):
                    for k in range(j, min(j + i, total_bits)):
                        if k != i:
                            parity ^= int(codeword[k])
                codeword[i] = str(parity)

        # Genel parite bitini hesapla
        overall_parity = 0
        for bit in codeword[1:]:
            overall_parity ^= int(bit)
        codeword[0] = str(overall_parity)

        return ''.join(codeword)

    def decode_hamming_secded(self, received):
        # Hamming SEC-DED kodunu çöz
        if not received:
            return None, "No data to decode"

        total_bits = len(received)
        syndrome = 0

        # Sendrom hesapla
        for i in range(total_bits):
            if self.is_power_of_2(i) and i != 0:
                parity = 0
                for j in range(i, total_bits, 2 * i):
                    for k in range(j, min(j + i, total_bits)):
                        parity ^= int(received[k])
                if parity != 0:
                    syndrome += i

        # Genel pariteyi hesapla
        overall_parity = 0
        for bit in received:
            overall_parity ^= int(bit)

        # Hata durumunu belirle
        if syndrome == 0 and overall_parity == 0:
            return self.extract_data_bits(received), "No error detected"
        elif syndrome != 0 and overall_parity != 0:
            return self.extract_data_bits(received), f"Single error detected at position {syndrome}"
        elif syndrome != 0 and overall_parity == 0:
            return None, "Double error detected (uncorrectable)"
        else:  # syndrome == 0 and overall_parity != 0
            return None, "Error in overall parity bit"

    def correct_single_error(self, received, error_position):
        # Tek bit hatayı düzelt
        if 0 <= error_position < len(received):
            corrected = list(received)
            corrected[error_position] = '1' if corrected[error_position] == '0' else '0'
            return ''.join(corrected)
        return received

    def extract_data_bits(self, codeword):
        # Veri bitlerini çıkar
        data_bits = []
        for i in range(1, len(codeword)):
            if not self.is_power_of_2(i):
                data_bits.append(codeword[i])
        return ''.join(data_bits)

    def calculate_parity_bits(self, data_bits):
        # Parite bit sayısını hesapla
        m = data_bits
        r = 1
        while (2 ** r) < (m + r + 1):
            r += 1
        return r + 1  # +1 for overall parity bit

    def is_power_of_2(self, n):
        # Sayının 2'nin kuvveti olup olmadığını kontrol et
        return n > 0 and (n & (n - 1)) == 0

    def get_current_code(self):
        # Mevcut kod durumunu döndür
        return self.current_code 