def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Direct_Bilirubin", "instances": 91, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 83, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=55.31325301204819:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 61, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=34.0655737704918:
                        # {"feature": "Alkaline_Phosphotase", "instances": 37, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>34.0655737704918:
                        # {"feature": "Alkaline_Phosphotase", "instances": 24, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>55.31325301204819:
                     # {"feature": "Alkaline_Phosphotase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[1]>4:
                           return 'liver'
                        elif obj[1]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>16:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'liver'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 26, "metric_value": 0.0, "depth": 5}
               if obj[5]>17:
                  # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": -0.0, "depth": 6}
                  if obj[4]>22:
                     # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=22:
                     # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=17:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Alkaline_Phosphotase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 28, "metric_value": 0.0, "depth": 5}
               if obj[8]<=12:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=40:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=35:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'normal'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>35:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>40:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>24:
                        return 'liver'
                     elif obj[4]<=24:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>12:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=41:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>41:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=20:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
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
            # {"feature": "Direct_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Total_Protiens", "instances": 69, "metric_value": 0.0, "depth": 5}
               if obj[6]>49.69565217391305:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=75.95652173913044:
                     # {"feature": "Alamine_Aminotransferase", "instances": 33, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=29.12121212121212:
                        # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>29.12121212121212:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>75.95652173913044:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=49.69565217391305:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=8:
                     # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=29:
                        # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=45:
                           return 'liver'
                        elif obj[4]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>29:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=21:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>21:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[5]>42:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>42:
                        return 'liver'
                     elif obj[4]<=42:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=6:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=42:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>5:
                     # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[6]>7:
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
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]<=35:
               # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[2]<=31.0:
                  return 'liver'
               elif obj[2]>31.0:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=196:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=173:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]>56:
                           return 'liver'
                        elif obj[6]<=56:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>173:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>196:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>35:
               # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[4]>30:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[1]>3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=63:
                           return 'liver'
                        elif obj[5]>63:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=30:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
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
               if obj[6]>59.265306122448976:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 69, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=306.76736428217924:
                     # {"feature": "Direct_Bilirubin", "instances": 66, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Total_Bilirubin", "instances": 52, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>3:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=227:
                           return 'liver'
                        elif obj[1]>227:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>306.76736428217924:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=59.265306122448976:
                  # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=11:
                     # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=78:
                           return 'liver'
                        elif obj[4]>78:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>26.155172413793103:
               # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[4]>18:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[6]>68:
                           return 'liver'
                        elif obj[6]<=68:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=18:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[2]<=1:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]<=15:
               # {"feature": "Total_Protiens", "instances": 35, "metric_value": 0.0, "depth": 5}
               if obj[6]>59:
                  # {"feature": "Alamine_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=147.78125:
                     # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=5:
                           return 'liver'
                        elif obj[2]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>147.78125:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=59:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>15:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[8]<=15:
                  # {"feature": "Alamine_Aminotransferase", "instances": 43, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=52.46511627906977:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Total_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=53:
                           return 'liver'
                        elif obj[1]>53:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>52.46511627906977:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=140:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>140:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>15:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>18:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=20:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>10:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'liver'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[5]>24:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[2]>12:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]>25:
                           return 'liver'
                        elif obj[1]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=12:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=5:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=24:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[8]<=1:
               # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 5}
               if obj[1]<=9:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=34:
                     # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>34:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Alkaline_Phosphotase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'normal'
                        elif obj[2]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>1:
               # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[4]<=29:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=23:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>23:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>12:
                        return 'normal'
                     elif obj[1]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]>29:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
