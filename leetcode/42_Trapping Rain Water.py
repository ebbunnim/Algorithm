class Solution:
    def trap(self, height: List[int]) -> int:
        # 변곡점일때, 작은 것들 다 밀어내고 그 밀어내는 것들 중 가장 차이가 작은 값을 더한다(trap)
        # trap 이 몇기간동안 존재했는지 알아야 한다.
        stack=[]
        ans=0
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                top = stack.pop()
                if stack==[]: # trap 할 수 없다.
                    break
                # 연산
                t = i-stack[-1]-1
                ans += (min(height[i],height[stack[-1]])-height[top])*t # 더 작은 높이의 기둥으로 trap
            stack.append(i)
        return ans