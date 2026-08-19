class Solution {

public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::map<char, int> s_map;
        std::map<char, int> t_map;

        for (int i = 0; i<s.length(); i++) s_map[s[i]] += 1;
        for (int i = 0; i<t.length(); i++) t_map[t[i]] += 1;

        bool cont_true = true;
        for (int i = 0; i<s.length(); i++) {
            char character = s[i];
            if (s_map[character] != t_map[character]) cont_true = false;
        }
        return cont_true;
    }
};
