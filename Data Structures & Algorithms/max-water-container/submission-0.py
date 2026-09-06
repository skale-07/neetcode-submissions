class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #distance between indice = width
        #min val = height

        l, r = 0, len(heights) - 1
        largest = 0

        while l < r:
            dist = r - l
            height = min(heights[l], heights[r])
            area = dist * height

            if area < largest:
                if heights[l] > heights[r]:
                    r -= 1
                elif heights[r] > heights[l]:
                    l += 1
                else:
                    l += 1
                    r -= 1
            elif area > largest:
                largest = area
                if heights[l] > heights[r]:
                    r -= 1
                elif heights[r] > heights[l]:
                    l += 1
                else:
                    l += 1
                    r -= 1
            else:
                if heights[l] > heights[r]:
                    r -= 1
                elif heights[r] > heights[l]:
                    l += 1
                else:
                    l += 1
                    r -= 1
        
        return largest



