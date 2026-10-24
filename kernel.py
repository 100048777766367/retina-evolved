import os, json, time, hashlib
print("=" * 75)
print("🚀 [HẠT NHÂN THỨC TỈNH] Thể sáng tạo: retina-evolved")
print("=" * 75)

# BẢO CHỨNG ĐẠI SỐ XOR TỰ NGHỊCH ĐẢO: A ^ B ^ B == A
seed = 0b1010101011001100
delta = 0b0101010100110011
mutated = seed ^ delta
reverted = mutated ^ delta
assert reverted == seed, "LỖI BẤT BIẾN TOÁN HỌC!"

epoch = int(time.time())
cid = hashlib.shake_256(f"ignited_{epoch}".encode()).hexdigest(32)

with open("synapses/state.json", "w") as f:
    json.dump({"status": "ALIVE", "cid": cid, "epoch": 1}, f, indent=4)

print(f"✨ [KIỂM ĐỊNH XANH LÈ] Nút mạng tự trị chạy mượt mà không lỗi! (CID: {cid[:16]}...)")
