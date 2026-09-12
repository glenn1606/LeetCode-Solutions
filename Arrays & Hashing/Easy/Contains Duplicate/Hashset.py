
nums = [1, 1, 3, 4, 2, 6, 8, 6, 7, 9, 0]

class Solution:
    def hasDuplicates (self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
s = Solution()
print(s.hasDuplicates(nums))

"""
seen = set()  # Khởi tạo set rỗng (Lưu ý: KHÔNG dùng {} vì đó là dict rỗng)
seen = set(nums)  # Chuyển một list thành set (loại bỏ phần tử trùng lặp ngay lập tức)
seen.add(val)  # Thêm phần tử val vào set - Độ phức tạp O(1)
if val in seen:  # Kiểm tra val có trong set hay không - Độ phức tạp O(1)
if val not in seen:  # Kiểm tra val KHÔNG có trong set - Độ phức tạp O(1)
seen.discard(val)  # Xóa val khỏi set; KHÔNG báo lỗi nếu val không tồn tại (Khuyên dùng)
seen.remove(val)  # Xóa val khỏi set; BÁO LỖI KeyError nếu val không tồn tại
len(seen)  # Trả về số lượng phần tử duy nhất hiện có trong set - Độ phức tạp O(1)"""
