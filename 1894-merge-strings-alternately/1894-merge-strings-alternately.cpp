class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged_word;
        int i;

        while (i < word1.length() && i < word2.length()){
            merged_word += word1[i];
            merged_word += word2[i];
            i++;
        }

        while (i < word1.length()){
            merged_word += word1[i];
            i++;
        }

        while (i < word2.length()){
            merged_word += word2[i];
            i++;
        }

        return merged_word;
    }
};