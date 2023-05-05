def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": -0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Aspartate_Aminotransferase", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[5]<=66.09401709401709:
               # {"feature": "Alkaline_Phosphotase", "instances": 87, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 71, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=16:
                     # {"feature": "Alamine_Aminotransferase", "instances": 66, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=27.696969696969695:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 41, "metric_value": 0.0, "depth": 8}
                        if obj[8]>8:
                           return 'liver'
                        elif obj[8]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>27.696969696969695:
                        # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>16:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=16:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[4]>19:
                           return 'liver'
                        elif obj[4]<=19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[1]>8:
                     return 'liver'
                  elif obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>66.09401709401709:
               # {"feature": "Alkaline_Phosphotase", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=68:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>68:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[4]>12:
               # {"feature": "Direct_Bilirubin", "instances": 34, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[1]>13:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=11:
                        return 'liver'
                     elif obj[8]>11:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=84:
                           return 'liver'
                        elif obj[5]>84:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=13:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[8]>8:
                           return 'normal'
                        elif obj[8]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[5]>12:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=96:
                           return 'liver'
                        elif obj[8]>96:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=6:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>30:
                           return 'normal'
                        elif obj[5]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[4]<=12:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[8]>6:
               # {"feature": "Total_Protiens", "instances": 46, "metric_value": 0.0, "depth": 5}
               if obj[6]>47.69565217391305:
                  # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=27:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>27:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]>5:
                           return 'normal'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>3:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[1]>13:
                        return 'liver'
                     elif obj[1]<=13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=49:
                           return 'normal'
                        elif obj[4]>49:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=47.69565217391305:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=45:
                           return 'liver'
                        elif obj[1]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]<=6:
               # {"feature": "Total_Protiens", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[6]>46.371428571428574:
                  # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=32:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]>30:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=30:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>32:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=46.371428571428574:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=33:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=29:
                        return 'liver'
                     elif obj[5]>29:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>33:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[4]<=139.2972972972973:
               # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 5}
               if obj[2]>7:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[5]>34:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=6:
                           return 'liver'
                        elif obj[8]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=34:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=7:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>5:
                        return 'liver'
                     elif obj[1]<=5:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=5:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]>139.2972972972973:
               # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 5}
               if obj[1]>11:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=6:
                     return 'liver'
                  elif obj[8]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[2]>3:
                        return 'liver'
                     elif obj[2]<=3:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=11:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[6]>63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 110, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 78, "metric_value": 0.0, "depth": 5}
               if obj[2]<=6:
                  # {"feature": "Total_Bilirubin", "instances": 62, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 41, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=116:
                        # {"feature": "Alamine_Aminotransferase", "instances": 36, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=36.44444444444444:
                           return 'normal'
                        elif obj[4]>36.44444444444444:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>116:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=87:
                           return 'liver'
                        elif obj[5]>87:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[4]>14:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'normal'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=14:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]>6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[5]>19:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=134:
                        # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=227:
                           return 'liver'
                        elif obj[1]>227:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>134:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=19:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[1]<=13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=55:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=56:
                           return 'normal'
                        elif obj[5]>56:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]>55:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]>108:
                           return 'liver'
                        elif obj[5]<=108:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[4]>74:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=500:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>500:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=74:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'liver'
                        elif obj[8]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 44, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=59:
                     # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>59:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=25:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[8]<=12.705263157894738:
            # {"feature": "Alkaline_Phosphotase", "instances": 82, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 58, "metric_value": 0.0, "depth": 5}
               if obj[6]>16.91673227394892:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 40, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=69.725:
                     # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>69.725:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[4]>56:
                        return 'liver'
                     elif obj[4]<=56:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=53:
                           return 'normal'
                        elif obj[1]>53:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=16.91673227394892:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>4:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[4]>38:
                  # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[6]>54:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>57:
                        return 'liver'
                     elif obj[5]<=57:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=54:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=9:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=38:
                  # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=11:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=34:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>34:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>11:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>21:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=47:
                           return 'normal'
                        elif obj[5]>47:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>12.705263157894738:
            # {"feature": "Total_Protiens", "instances": 13, "metric_value": 0.0, "depth": 4}
            if obj[6]>7:
               # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[5]>20:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=55:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>5:
                           return 'liver'
                        elif obj[2]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>55:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=20:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=7:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
