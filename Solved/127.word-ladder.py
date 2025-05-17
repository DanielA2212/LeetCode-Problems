#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

from collections import deque
# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        word_set=set(wordList)

        if endWord not in word_set or beginWord==endWord:
            return 0
        
        alphabet='abcdefghijklmnopqrstuvwxyz'
        word_queue=deque()
        word_queue.append((beginWord,1))

        # Bfs, adding to queue the first word and initial amount of transformations
        while word_queue:
            current_word,transformation_amount=word_queue.popleft()

            for i in range(len(current_word)):
                for char in alphabet:
                    # Breaking the current word at i and adding a new char at position i
                    new_word=current_word[:i]+char+current_word[i+1:]
                    
                    if new_word in word_set:
                        if new_word==endWord:
                            return transformation_amount+1
                        
                        word_queue.append((new_word,transformation_amount+1))
                        word_set.remove(new_word)

        # Cannot find a transformation                
        return 0
# @lc code=end

