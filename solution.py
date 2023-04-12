import pandas as pd
import numpy as np


chat_id = 808572568 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    def z_test(P1, P2, n1, n2):
      P0 = (P1 * n1 + P2 * n2) / (n1 + n2)
      Z = (P1 - P2) / np.sqrt((P0 * (1 - P0)) * ((1 / n1) + (1 / n2)))
      return Z

    P1 = x_success / x_cnt
    P2 = y_success / y_cnt
    N = x_cnt + y_cnt
    
    Z = z_test(P1, P2, x_cnt, y_cnt)
    
    flag = 0
    if Z > 1.28:
      flag = 1

    return flag # Ваш ответ, True или False
