def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Direct_Bilirubin", "instances": 233, "metric_value": 0.0, "depth": 3}
         if obj[2]>1:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 204, "metric_value": 0.0, "depth": 4}
            if obj[8]<=151.09441352744844:
               # {"feature": "Age", "instances": 198, "metric_value": 0.0, "depth": 5}
               if obj[0]<=58.57064762156122:
                  # {"feature": "Total_Protiens", "instances": 162, "metric_value": 0.0, "depth": 6}
                  if obj[6]>15.96269296532256:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 141, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=100.71631205673759:
                        # {"feature": "Total_Bilirubin", "instances": 121, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=13.49586776859504:
                           return 'liver'
                        elif obj[1]>13.49586776859504:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>100.71631205673759:
                        # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=15.96269296532256:
                     # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=32:
                           return 'normal'
                        elif obj[5]>32:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[0]>58.57064762156122:
                  # {"feature": "Total_Protiens", "instances": 36, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=67:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=40:
                           return 'liver'
                        elif obj[5]>40:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>67:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=42:
                           return 'normal'
                        elif obj[4]>42:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>151.09441352744844:
               # {"feature": "Age", "instances": 6, "metric_value": -0.0, "depth": 5}
               if obj[0]>29:
                  # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=6:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[0]<=29:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]>36:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=1:
                        return 'normal'
                     elif obj[1]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=36:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[2]<=1:
            # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 4}
            if obj[1]<=7:
               # {"feature": "Age", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[0]>13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=32:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]>12:
                        # {"feature": "Total_Protiens", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=73:
                           return 'liver'
                        elif obj[6]>73:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>32:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=33:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]>11:
                           return 'normal'
                        elif obj[8]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>33:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[0]<=13:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]>7:
               # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[6]>59:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=1:
                     return 'liver'
                  elif obj[8]>1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=59:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 73, "metric_value": -0.0, "depth": 3}
         if obj[0]>21.507241829988953:
            # {"feature": "Total_Protiens", "instances": 58, "metric_value": -0.0, "depth": 4}
            if obj[6]>63.706896551724135:
               # {"feature": "Alamine_Aminotransferase", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[4]>24:
                  # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=53.71052631578947:
                     # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=18:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[8]>8:
                           return 'liver'
                        elif obj[8]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>53.71052631578947:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=24:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=63.706896551724135:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[8]<=8:
                  return 'liver'
               elif obj[8]>8:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=20:
                           return 'liver'
                        elif obj[4]>20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]<=21.507241829988953:
            # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 4}
            if obj[1]<=15:
               # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 5}
               if obj[5]<=56:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[8]>7:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=21:
                           return 'normal'
                        elif obj[4]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>56:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=25:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>15:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Total_Protiens", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[6]>22.141963590857678:
         # {"feature": "Alkaline_Phosphotase", "instances": 163, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Age", "instances": 115, "metric_value": 0.0, "depth": 4}
            if obj[0]<=46.08695652173913:
               # {"feature": "Direct_Bilirubin", "instances": 64, "metric_value": 0.0, "depth": 5}
               if obj[2]<=18.984375:
                  # {"feature": "Total_Bilirubin", "instances": 50, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 38, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=43.10526315789474:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=45:
                           return 'liver'
                        elif obj[8]>45:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>43.10526315789474:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=140:
                           return 'liver'
                        elif obj[5]>140:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=45:
                           return 'liver'
                        elif obj[4]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'normal'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>18.984375:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=7:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]>68:
                        return 'liver'
                     elif obj[1]<=68:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>32:
                           return 'liver'
                        elif obj[4]<=32:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]>46.08695652173913:
               # {"feature": "Direct_Bilirubin", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=194.1793597539379:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=220.46023322258708:
                           return 'liver'
                        elif obj[5]>220.46023322258708:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>194.1793597539379:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[2]<=2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=12:
                     # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=35:
                           return 'liver'
                        elif obj[4]>35:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>28:
                        return 'liver'
                     elif obj[5]<=28:
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
            # {"feature": "Direct_Bilirubin", "instances": 48, "metric_value": 0.0, "depth": 4}
            if obj[2]<=75.49460750103084:
               # {"feature": "Age", "instances": 38, "metric_value": -0.0, "depth": 5}
               if obj[0]>13:
                  # {"feature": "Total_Bilirubin", "instances": 37, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 36, "metric_value": -0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=37:
                           return 'liver'
                        elif obj[8]>37:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[0]<=13:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]>75.49460750103084:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[6]<=22.141963590857678:
         # {"feature": "Alkaline_Phosphotase", "instances": 50, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Age", "instances": 36, "metric_value": 0.0, "depth": 4}
            if obj[0]>18:
               # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'normal'
                        elif obj[5]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=9:
                        return 'liver'
                     elif obj[8]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=114:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=13:
                           return 'liver'
                        elif obj[2]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=20:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>114:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=18:
               return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Age", "instances": 14, "metric_value": 0.0, "depth": 4}
            if obj[0]>41:
               return 'liver'
            elif obj[0]<=41:
               # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 5}
               if obj[1]>12:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]>4:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=4:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[1]<=12:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
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
