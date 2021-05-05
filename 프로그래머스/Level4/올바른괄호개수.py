import time

def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

def solution(n):
    nums=[1]*n+[2]*n
    @logging_time
    def validate(stringfy_stack):
        stack=list(map(int,stringfy_stack))
        stack2=[]
        if stack[-1]!=2: # 1-열린 괄호, 2-닫힌 괄호
            return False
        # 괄호 쌍은 지금 확보가 된 상황임.
        while stack:
            print('=-=-=-==-=-=--=-=-=-==-=-=-=')
            stack2+=[stack.pop()]
            while stack and stack2:
                s=stack[-1]
                e=stack2[-1]
                if e==2 and s==1: # 3으로 된다고 하면?
                    stack.pop()
                    stack2.pop()
                else:
                    break
        if stack2==[]:
            return True
        return False
    vis=[False]*(2*n)
    ans=set()
    @logging_time
    def dfs(cnt,stack): # input:sidx, cnt
        if cnt==2*n:
            # validate
            stringfy_stack=''.join(map(str,stack))
            if validate(stringfy_stack):
                ans.add(stringfy_stack)
            return
        for i in range(2*n):
            if vis[i]==False:
                stack+=[nums[i]]
                vis[i]=True
                dfs(cnt+1,stack)
                vis[i]=False
                stack.pop()
        return
    dfs(0,[])
    return len(ans)
solution(14)