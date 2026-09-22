class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # [0][0], [0][1], [0][2]
        # [1][0], [1][1], [1][2]
        # [2][0], [2][1], [2][2]

        # [6][6], [6][7], [6][8]
        # [7][6], [7][7], [7][8]
        # [8][6], [8][7], [8][8]

        # 0 1 2 3 4 5 6 7 8
        # 0 0 0 1 1 1 2 2 2
        # 0 0 0 1 1 1 2 2 2
        # 0 0 0 1 1 1 2 2 2
        # 3 3 3 4 4 4 5 5 5
        new_board = []
        ver = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        box_pointer = 0

        for i in range(0, 9):
            row = set()
            for j in range(0, 9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in row:
                        # print('F1')
                        return False
                    if num in ver[j]:
                        # print('F2')
                        return False
                    else:
                        if box_pointer < 27:
                            if num in box[(j // 3)]:
                                # print('F3', i, j, box_pointer)
                                return False
                            else:
                                box[(j // 3)].add(num)
                                # print('Box ', (j // 3) , box[(j // 3)])
                        elif box_pointer >= 27 and box_pointer < 54:
                            if num in box[(j // 3)+3]:
                                # print('F4', i, j, box_pointer)
                                # print('Box ', (j // 3)+3 , box[(j // 3)+3])
                                return False
                            else:
                                box[(j // 3)+3].add(num)
                                # print('Box ', (j // 3)+3 , box[(j // 3)+3])
                        else:
                            if num in box[(j // 3)+6]:
                                # print('F5')
                                return False
                            else:
                                box[(j // 3)+6].add(num)
                                # print('Box ', (j // 3)+6 , box[(j // 3)+6])
                                # print(box[(j // 3)+6])
                        row.add(num)
                        ver[j].add(num)
                box_pointer += 1

            new_board.append(row)

        
        return True


                
                    



