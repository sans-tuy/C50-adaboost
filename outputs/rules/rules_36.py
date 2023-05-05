def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]<=81.47896483100102:
            # {"feature": "Aspartate_Aminotransferase", "instances": 144, "metric_value": 0.0, "depth": 4}
            if obj[5]<=63.36805555555556:
               # {"feature": "Direct_Bilirubin", "instances": 106, "metric_value": 0.0, "depth": 5}
               if obj[2]<=6:
                  # {"feature": "Total_Bilirubin", "instances": 89, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 70, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=27.12857142857143:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 46, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=13:
                           return 'liver'
                        elif obj[8]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>27.12857142857143:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=116:
                           return 'liver'
                        elif obj[8]>116:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=38:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[8]>11:
                           return 'normal'
                        elif obj[8]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>38:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>6:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=13:
                     # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>13:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]>63.36805555555556:
               # {"feature": "Alkaline_Phosphotase", "instances": 38, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[1]>4:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=14:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]>33:
                           return 'liver'
                        elif obj[4]<=33:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>14:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=4:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]>81.47896483100102:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 4}
            if obj[8]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[4]>22:
                     return 'liver'
                  elif obj[4]<=22:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>1:
               # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'normal'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>47.123456790123456:
               # {"feature": "Total_Bilirubin", "instances": 54, "metric_value": 0.0, "depth": 5}
               if obj[1]<=30.944444444444443:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 41, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=39.457142857142856:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>39.457142857142856:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>30.944444444444443:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=47.123456790123456:
               # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=74:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>74:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>30:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=30:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[4]>15:
                           return 'normal'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=53:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        return 'liver'
                     elif obj[1]>6:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>53:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]<=13:
               # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[2]<=31.896551724137932:
                  return 'liver'
               elif obj[2]>31.896551724137932:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[6]>56:
                     return 'liver'
                  elif obj[6]<=56:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=88:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=73:
                           return 'normal'
                        elif obj[1]>73:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>88:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>13:
               # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=35:
                     return 'liver'
                  elif obj[4]>35:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>67:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'normal'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=67:
                        return 'liver'
                     else:
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
            if obj[8]>1:
               # {"feature": "Direct_Bilirubin", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 6}
                  if obj[6]>61.160493827160494:
                     # {"feature": "Alamine_Aminotransferase", "instances": 61, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=69.40983606557377:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 50, "metric_value": 0.0, "depth": 8}
                        if obj[5]>11:
                           return 'liver'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>69.40983606557377:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=61.160493827160494:
                     # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=52:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>52:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>35:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=69:
                           return 'liver'
                        elif obj[6]>69:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=35:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=31:
                           return 'liver'
                        elif obj[5]>31:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=25:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>71:
                           return 'liver'
                        elif obj[6]<=71:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>25:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=35:
                           return 'liver'
                        elif obj[4]>35:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[4]>25:
                  # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[6]>66:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>24:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=24:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=66:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>26:
                        return 'liver'
                     elif obj[5]<=26:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=25:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>12:
                           return 'normal'
                        elif obj[5]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
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
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]<=11:
               # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[6]<=71:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[5]>139:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[4]>152:
                        return 'liver'
                     elif obj[4]<=152:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=139:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]>71:
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=29:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'normal'
                        elif obj[5]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'normal'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>29:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>34:
                           return 'liver'
                        elif obj[5]<=34:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[8]>11:
               # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[4]>26:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=26:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
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
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>19.418485261141242:
            # {"feature": "Alkaline_Phosphotase", "instances": 69, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[1]<=36.92156862745098:
                  # {"feature": "Direct_Bilirubin", "instances": 40, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=44.625:
                        # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=43:
                           return 'normal'
                        elif obj[4]>43:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>44.625:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[8]>7:
                           return 'liver'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[8]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>27:
                           return 'liver'
                        elif obj[5]<=27:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>36.92156862745098:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=5:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=45:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=61:
                           return 'liver'
                        elif obj[5]>61:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>45:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>5:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]>23:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=16:
                           return 'normal'
                        elif obj[2]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=23:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>28:
                        return 'normal'
                     elif obj[1]<=28:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[8]>8:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=19.418485261141242:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 4}
            if obj[8]<=5:
               # {"feature": "Alkaline_Phosphotase", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=21:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>29:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'normal'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=29:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>4:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>13:
                        return 'liver'
                     elif obj[1]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=4:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[8]>5:
               # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=850:
                           return 'liver'
                        elif obj[5]>850:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
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
