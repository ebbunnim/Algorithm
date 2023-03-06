class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
        for (int num=1;num<=n;num++) {
            ans.push_back(getResult(num));
        }
        return ans;
    }

    string getResult(int num) {
        if (num%3==0 && num%5==0) 
            return "FizzBuzz";
        else if (num%3==0) 
            return "Fizz";
        else if (num%5==0)
            return "Buzz";
        else
            return to_string(num);
    }
};