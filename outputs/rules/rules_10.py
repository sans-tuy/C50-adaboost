def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 233, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 185, "metric_value": 0.0, "depth": 4}
            if obj[6]>58.90810810810811:
               # {"feature": "Age", "instances": 143, "metric_value": 0.0, "depth": 5}
               if obj[0]<=59.143783050011564:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 113, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=65.84070796460178:
                     # {"feature": "Alamine_Aminotransferase", "instances": 87, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=29.114942528735632:
                        # {"feature": "Total_Bilirubin", "instances": 52, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>29.114942528735632:
                        # {"feature": "Direct_Bilirubin", "instances": 35, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>65.84070796460178:
                     # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=91:
                           return 'liver'
                        elif obj[4]>91:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[0]>59.143783050011564:
                  # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=21:
                           return 'liver'
                        elif obj[5]>21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]>14:
                           return 'liver'
                        elif obj[5]<=14:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>11:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=85:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>85:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=58.90810810810811:
               # {"feature": "Age", "instances": 42, "metric_value": -0.0, "depth": 5}
               if obj[0]<=44.26190476190476:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=180:
                     # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=78:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>78:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>180:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[0]>44.26190476190476:
                  # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5]>22:
                           return 'normal'
                        elif obj[5]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=45:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'normal'
                        elif obj[5]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>45:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[1]>11:
                           return 'liver'
                        elif obj[1]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Age", "instances": 48, "metric_value": 0.0, "depth": 4}
            if obj[0]<=57.44569923452688:
               # {"feature": "Total_Protiens", "instances": 39, "metric_value": 0.0, "depth": 5}
               if obj[6]<=85.70183348271345:
                  # {"feature": "Direct_Bilirubin", "instances": 36, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=19:
                        # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>19:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'liver'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>14:
                        return 'liver'
                     elif obj[4]<=14:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]>85.70183348271345:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]>31:
                     return 'liver'
                  elif obj[4]<=31:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[0]>57.44569923452688:
               # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 5}
               if obj[5]<=37:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'normal'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>37:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 73, "metric_value": 0.0, "depth": 3}
         if obj[0]<=40.63013698630137:
            # {"feature": "Alamine_Aminotransferase", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[4]<=125.10810810810811:
               # {"feature": "Total_Protiens", "instances": 26, "metric_value": 0.0, "depth": 5}
               if obj[6]>69:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[5]>35:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=35:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=69:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=16:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>16:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>125.10810810810811:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        return 'normal'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[8]<=1:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]>40.63013698630137:
            # {"feature": "Total_Protiens", "instances": 36, "metric_value": -0.0, "depth": 4}
            if obj[6]>62:
               # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 5}
               if obj[1]<=76.04347826086956:
                  # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     return 'liver'
                  elif obj[4]<=25:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>76.04347826086956:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=62:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Age", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[0]<=45.63576158940398:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[8]<=7:
               # {"feature": "Total_Protiens", "instances": 42, "metric_value": -0.0, "depth": 5}
               if obj[6]>36:
                  # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=45:
                     # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>45:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=36:
                  # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=20:
                           return 'liver'
                        elif obj[5]>20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>6:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>16:
                        return 'liver'
                     elif obj[1]<=16:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>7:
               # {"feature": "Direct_Bilirubin", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Protiens", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=81:
                     # {"feature": "Alamine_Aminotransferase", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=47.30769230769231:
                        # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>47.30769230769231:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]>41:
                           return 'liver'
                        elif obj[5]<=41:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]>81:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>2:
                  # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[1]>11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=168:
                           return 'liver'
                        elif obj[5]>168:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=11:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]>45.63576158940398:
            # {"feature": "Alamine_Aminotransferase", "instances": 70, "metric_value": -0.0, "depth": 4}
            if obj[4]<=41.94285714285714:
               # {"feature": "Direct_Bilirubin", "instances": 50, "metric_value": -0.0, "depth": 5}
               if obj[2]<=5:
                  # {"feature": "Total_Bilirubin", "instances": 34, "metric_value": -0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=16:
                        # {"feature": "Total_Protiens", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[6]>38:
                           return 'liver'
                        elif obj[6]<=38:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'liver'
                        elif obj[5]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Total_Protiens", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[6]>48:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>5:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 6}
                  if obj[5]>12:
                     return 'liver'
                  elif obj[5]<=12:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]>41.94285714285714:
               # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[5]>25:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=7:
                        return 'liver'
                     elif obj[8]>7:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[6]>5:
                           return 'liver'
                        elif obj[6]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=25:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 62, "metric_value": -0.0, "depth": 3}
         if obj[8]<=6:
            # {"feature": "Total_Protiens", "instances": 35, "metric_value": -0.0, "depth": 4}
            if obj[6]>6:
               # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[1]<=87.51612903225806:
                  # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=32:
                     # {"feature": "Age", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[0]>32:
                        # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[0]<=32:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>34:
                           return 'liver'
                        elif obj[5]<=34:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>32:
                     # {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[0]<=50:
                        return 'normal'
                     elif obj[0]>50:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]>87.51612903225806:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=6:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[2]>4:
                  # {"feature": "Age", "instances": 3, "metric_value": -0.0, "depth": 6}
                  if obj[0]>18:
                     return 'liver'
                  elif obj[0]<=18:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[2]<=4:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[8]>6:
            # {"feature": "Total_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 4}
            if obj[1]<=31.48148148148148:
               # {"feature": "Age", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[0]<=42:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[5]>25:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=48:
                        return 'liver'
                     elif obj[4]>48:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=12:
                           return 'normal'
                        elif obj[2]>12:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[5]<=25:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[0]>42:
                  # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]>20:
                        return 'liver'
                     elif obj[4]<=20:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'normal'
                        elif obj[5]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>11:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>31.48148148148148:
               # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[2]<=76:
                  # {"feature": "Age", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[0]>50:
                     return 'liver'
                  elif obj[0]<=50:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>52:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=50:
                           return 'liver'
                        elif obj[5]>50:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=52:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>76:
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
