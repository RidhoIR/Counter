import redis

# Buat koneksi ke server Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Nama kunci untuk counter
counter_key = 'my_counter'

# Fungsi untuk increment counter
def increment_counter():
    return r.incr(counter_key)

# Penggunaan contoh
incremented_value = increment_counter()
print(f'Incremented Counter Value: {incremented_value}')
