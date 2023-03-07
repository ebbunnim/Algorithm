// Solution 1
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> uMap = constructMap(magazine);
        for (int idx=0; idx<ransomNote.size(); idx++) {
            if (uMap.find(ransomNote[idx])!=uMap.end()) {
                if (--uMap[ransomNote[idx]]<0)
                    return false;
            } else {
                return false;
            }
        }
        return true;
    }

    unordered_map<char, int> constructMap(string magazine) {
        unordered_map<char, int> uMap;
        for (int idx=0; idx<magazine.size(); idx++) {
            if (uMap.find(magazine[idx])!=uMap.end()) 
                uMap[magazine[idx]]++;
            else 
                uMap[magazine[idx]]=1;
        }
        return uMap;
    }; 

};

// Solution2
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int cnt[26] = {0};
        for (int idx=0; idx<magazine.size(); idx++) {
            cnt[magazine[idx]-'a']++;
        }
        for (int idx=0; idx<ransomNote.size(); idx++) {
            if (--cnt[ransomNote[idx]-'a']<0) 
                return false;
        }
        return true;
    }

};