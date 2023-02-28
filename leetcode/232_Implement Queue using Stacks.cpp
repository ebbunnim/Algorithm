class MyQueue {
public:
    stack<int> stack;
    stack<int> stackForQueue;

    MyQueue() {}
    
    void push(int x) {
        while (!stackForQueue.empty()) {
            stack.push(stackForQueue.top());
            stackForQueue.pop();  // python과 다르게 pop된 원소를 반환하지 않는다.
        }
        stack.push(x);
        while (!stack.empty()) {
            stackForQueue.push(stack.top());
            stack.pop();  
        }
    }
    
    int pop() {
        int top = stackForQueue.top();
        stackForQueue.pop();
        return top;
    }
    
    int peek() {
        return stackForQueue.top();
    }
    
    bool empty() {
        return stackForQueue.empty();

    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */