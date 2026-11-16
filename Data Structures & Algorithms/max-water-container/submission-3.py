class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0
        min_height=min(heights[r],heights[l])
        min_width = r-l
        while(l<r):
            current_area= (r-l)* min(heights[r],heights[l])
            if current_area > max_area:
                min_height=min(heights[r],heights[l])
                min_width = r-l
                max_area= current_area
                if heights[r]>heights[l]:
                    l+=1
                else:
                    r-=1
            else:
                # if max_area // min_width > r-l:
                #     break
                # else:
                if heights[r]>heights[l]:
                    l+=1
                else:
                    r-=1
        return max_area