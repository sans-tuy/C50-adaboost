def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Aspartate_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[5]<=63.19078947368421:
            # {"feature": "Alamine_Aminotransferase", "instances": 112, "metric_value": 0.0, "depth": 4}
            if obj[4]<=30.285714285714285:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 69, "metric_value": 0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Alkaline_Phosphotase", "instances": 42, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 36, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Total_Protiens", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[6]>64:
                           return 'liver'
                        elif obj[6]<=64:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>8:
                        # {"feature": "Total_Protiens", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[6]>61:
                           return 'liver'
                        elif obj[6]<=61:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Total_Protiens", "instances": 17, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=66:
                           return 'normal'
                        elif obj[6]>66:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>4:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=11:
                           return 'normal'
                        elif obj[1]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]>30.285714285714285:
               # {"feature": "Total_Protiens", "instances": 43, "metric_value": 0.0, "depth": 5}
               if obj[6]>59.325581395348834:
                  # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 29, "metric_value": -0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=12:
                           return 'liver'
                        elif obj[1]>12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=59.325581395348834:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=87:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>87:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[5]>63.19078947368421:
            # {"feature": "Alkaline_Phosphotase", "instances": 40, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": 0.0, "depth": 5}
               if obj[8]<=13:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[1]>4:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[4]>61:
                        return 'liver'
                     elif obj[4]<=61:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>6:
                           return 'liver'
                        elif obj[2]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=4:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>13:
                  # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=60:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=17:
                           return 'normal'
                        elif obj[1]>17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>60:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=3:
                     # {"feature": "Total_Protiens", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[6]>5:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=5:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]<=70.5999397517626:
               # {"feature": "Alamine_Aminotransferase", "instances": 68, "metric_value": -0.0, "depth": 5}
               if obj[4]<=38.294117647058826:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 44, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 30, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=92.76734606777677:
                        # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>92.76734606777677:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]>29:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=29:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=22:
                           return 'liver'
                        elif obj[1]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>38.294117647058826:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[5]>25:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=11:
                        # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=21:
                           return 'liver'
                        elif obj[1]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=25:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>70.5999397517626:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[8]>4:
                  return 'liver'
               elif obj[8]<=4:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=44:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>14:
                           return 'liver'
                        elif obj[4]<=14:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>44:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Aspartate_Aminotransferase", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[5]<=310.7837837837838:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 28, "metric_value": 0.0, "depth": 5}
               if obj[8]<=35:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[1]>24:
                     # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=56:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[4]>43:
                           return 'liver'
                        elif obj[4]<=43:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>56:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=24:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>35:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=35:
                           return 'liver'
                        elif obj[4]>35:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>5:
                        return 'liver'
                     elif obj[1]<=5:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>310.7837837837838:
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
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[8]<=26.155172413793103:
               # {"feature": "Total_Protiens", "instances": 98, "metric_value": -0.0, "depth": 5}
               if obj[6]<=84.2058685354684:
                  # {"feature": "Total_Bilirubin", "instances": 91, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=24.428571428571427:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 74, "metric_value": 0.0, "depth": 7}
                     if obj[5]>11:
                        # {"feature": "Direct_Bilirubin", "instances": 73, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=7:
                           return 'liver'
                        elif obj[2]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>24.428571428571427:
                     # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=171:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[4]>80:
                           return 'liver'
                        elif obj[4]<=80:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>171:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>84.2058685354684:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=7:
                     return 'liver'
                  elif obj[1]>7:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'normal'
                        elif obj[4]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>26.155172413793103:
               # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[4]>19:
                  # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[6]>68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=87:
                        return 'liver'
                     elif obj[5]>87:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=68:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]<=19:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[6]>69:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[8]<=9:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=500:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=35:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=16:
                           return 'liver'
                        elif obj[2]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>35:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>500:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>9:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]<=69:
               # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[4]>70:
                     return 'liver'
                  elif obj[4]<=70:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=25:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 7}
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
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": -0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 63, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 5}
               if obj[4]<=53.91304347826087:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 6}
                  if obj[5]>10:
                     # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>16:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>23:
                           return 'liver'
                        elif obj[2]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]>53.91304347826087:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[8]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]>90:
                        return 'liver'
                     elif obj[5]<=90:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]<=7:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>82:
                           return 'liver'
                        elif obj[2]<=82:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[5]>76:
                  return 'liver'
               elif obj[5]<=76:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[4]>37:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>21:
                        return 'normal'
                     elif obj[1]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=37:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>15:
                           return 'normal'
                        elif obj[2]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=9:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=44.49473684210526:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[8]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[5]>23:
                        return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=62:
                           return 'liver'
                        elif obj[5]>62:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>48:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>1:
               # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[1]<=11:
                  # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>21:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=21:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]>11:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=10:
                           return 'normal'
                        elif obj[4]>10:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
