def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Direct_Bilirubin", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[2]>1:
            # {"feature": "Alamine_Aminotransferase", "instances": 136, "metric_value": 0.0, "depth": 4}
            if obj[4]<=52.169117647058826:
               # {"feature": "Total_Protiens", "instances": 97, "metric_value": 0.0, "depth": 5}
               if obj[6]<=82.69678293509746:
                  # {"feature": "Alkaline_Phosphotase", "instances": 92, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 78, "metric_value": -0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 53, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=31.641509433962263:
                           return 'liver'
                        elif obj[5]>31.641509433962263:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=9:
                        # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>82.69678293509746:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=58:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>58:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>52.169117647058826:
               # {"feature": "Alkaline_Phosphotase", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[5]>41:
                     # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[1]>22:
                        return 'liver'
                     elif obj[1]<=22:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'liver'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=41:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[2]<=1:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": 0.0, "depth": 4}
            if obj[8]>8:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]>20:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>16:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>6:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>22:
                           return 'normal'
                        elif obj[5]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=20:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=21:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[5]>21:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=7:
                        return 'liver'
                     elif obj[1]>7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[8]<=8:
               # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[6]>58:
                        return 'liver'
                     elif obj[6]<=58:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=14:
                           return 'normal'
                        elif obj[4]>14:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": -0.0, "depth": 4}
            if obj[6]>23.646973828484313:
               # {"feature": "Alamine_Aminotransferase", "instances": 64, "metric_value": 0.0, "depth": 5}
               if obj[4]<=38.71875:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 42, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=38.708333333333336:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>38.708333333333336:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=32:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>32:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>38.71875:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[2]>4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]>32:
                           return 'liver'
                        elif obj[5]<=32:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=4:
                           return 'liver'
                        elif obj[1]>4:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=23.646973828484313:
               # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[8]>1:
                     return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     return 'liver'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]<=91.43074028249146:
               # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[1]<=53.08571428571429:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=13:
                     return 'liver'
                  elif obj[8]>13:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        return 'liver'
                     elif obj[4]<=20:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[5]>28:
                           return 'normal'
                        elif obj[5]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>53.08571428571429:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[4]>88:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=5:
                        return 'liver'
                     elif obj[8]>5:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>285:
                           return 'liver'
                        elif obj[5]<=285:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=88:
                     # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=51:
                        return 'liver'
                     elif obj[6]>51:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=5:
                           return 'liver'
                        elif obj[8]>5:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>91.43074028249146:
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
            # {"feature": "Aspartate_Aminotransferase", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[5]>11:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 115, "metric_value": 0.0, "depth": 5}
               if obj[8]<=26.286956521739132:
                  # {"feature": "Total_Bilirubin", "instances": 97, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Total_Protiens", "instances": 89, "metric_value": 0.0, "depth": 7}
                     if obj[6]>59.28089887640449:
                        # {"feature": "Direct_Bilirubin", "instances": 62, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=7:
                           return 'liver'
                        elif obj[2]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=59.28089887640449:
                        # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=295.0740740740741:
                           return 'liver'
                        elif obj[4]>295.0740740740741:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'normal'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>26.286956521739132:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>35:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=35:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>61:
                           return 'normal'
                        elif obj[6]<=61:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>36:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=19:
                           return 'liver'
                        elif obj[1]>19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=36:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>12:
                           return 'liver'
                        elif obj[1]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]<=11:
               return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]<=16:
               # {"feature": "Total_Protiens", "instances": 36, "metric_value": 0.0, "depth": 5}
               if obj[6]<=72:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=39:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[4]>68:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=4:
                           return 'liver'
                        elif obj[2]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=68:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>39:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>72:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>42:
                           return 'liver'
                        elif obj[5]<=42:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>16:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[6]>19.155279749709432:
               # {"feature": "Direct_Bilirubin", "instances": 51, "metric_value": -0.0, "depth": 5}
               if obj[2]<=7:
                  # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=76:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 8}
                        if obj[5]>17:
                           return 'normal'
                        elif obj[5]<=17:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>76:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=31:
                           return 'normal'
                        elif obj[4]>31:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[4]>18:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=56:
                           return 'liver'
                        elif obj[5]>56:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>7:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[1]>68:
                     return 'liver'
                  elif obj[1]<=68:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>32:
                        return 'liver'
                     elif obj[4]<=32:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=19.155279749709432:
               # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[4]>25:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=7:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>7:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=25:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=20:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>20:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
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
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": -0.0, "depth": 4}
            if obj[6]>54:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[4]>38:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=121:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=57:
                           return 'normal'
                        elif obj[5]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>121:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=38:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>22:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'normal'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=22:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>8:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=54:
               # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        return 'liver'
                     elif obj[4]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>3:
                           return 'normal'
                        elif obj[2]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[8]<=1:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>4:
                        return 'liver'
                     elif obj[2]<=4:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>30:
                        return 'liver'
                     elif obj[4]<=30:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>2:
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
