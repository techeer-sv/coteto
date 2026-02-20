#include <string>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    array<int, 5> s1 = {1,2,3,4,5};
    array<int, 8> s2 = {2,1,2,3,2,4,2,5};
    array<int, 10> s3 = {3,3,1,1,2,2,4,4,5,5};
    
    array<int, 3> score = {0, 0, 0};
    
    vector<int>::iterator ptr;
    int idx = 0;
    for (ptr = answers.begin(); ptr != answers.end(); ++ptr) {
        int num = *ptr;
        if (num == s1[idx%5]) {
            score[0] += 1;   
        }
        if (num == s2[idx%8]) {
            score[1] += 1;  
        }
        if (num == s3[idx%10]) {
            score[2] += 1;   
        }
        idx += 1;
    }
        
    int max = 0;
    for (int i =0; i<3; i++) {
        if (score[i]>max){
            max = score[i];
        }
    }
    
    for (int i=0; i<3; i++) {
        if (max == score[i]) {
            answer.push_back(i+1);
        }
    }
    
    sort(answer.begin(), answer.end());
    
    return answer;
}