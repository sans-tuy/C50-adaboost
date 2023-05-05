def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>60.46052631578947:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 91, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 67, "metric_value": 0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Total_Bilirubin", "instances": 66, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13.727272727272727:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 50, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=40.1:
                           return 'liver'
                        elif obj[5]>40.1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>13.727272727272727:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[5]>51:
                           return 'liver'
                        elif obj[5]<=51:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     return 'liver'
                  elif obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=49:
                     # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alkaline_Phosphotase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>49:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.46052631578947:
            # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[4]<=42.885714285714286:
               # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 5}
               if obj[5]>14:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=11:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>11:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=14:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'normal'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[4]>42.885714285714286:
               # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 5}
               if obj[5]>40:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=14:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[1]>17:
                        return 'liver'
                     elif obj[1]<=17:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>14:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=40:
                  # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=2:
                        return 'liver'
                     elif obj[1]>2:
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
         # {"feature": "Direct_Bilirubin", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[2]>1:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 102, "metric_value": -0.0, "depth": 4}
            if obj[8]<=14.049019607843137:
               # {"feature": "Total_Protiens", "instances": 87, "metric_value": -0.0, "depth": 5}
               if obj[6]>50.62068965517241:
                  # {"feature": "Alkaline_Phosphotase", "instances": 58, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 41, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Total_Bilirubin", "instances": 40, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=38.375:
                           return 'liver'
                        elif obj[1]>38.375:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=86:
                           return 'liver'
                        elif obj[1]>86:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=50.62068965517241:
                  # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>30:
                           return 'liver'
                        elif obj[5]<=30:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[5]>25:
                        return 'liver'
                     elif obj[5]<=25:
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
            elif obj[8]>14.049019607843137:
               # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[5]>32:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=33:
                        return 'liver'
                     elif obj[4]>33:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=18:
                           return 'liver'
                        elif obj[4]>18:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=32:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[6]>52:
                        return 'liver'
                     elif obj[6]<=52:
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
         elif obj[2]<=1:
            # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 4}
            if obj[5]>23:
               # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[8]>5:
                        # {"feature": "Total_Protiens", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=5:
                           return 'liver'
                        elif obj[6]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=5:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=20:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     return 'liver'
                  elif obj[1]<=5:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]<=23:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Protiens", "instances": 81, "metric_value": -0.0, "depth": 6}
                  if obj[6]>17.273482007808447:
                     # {"feature": "Total_Bilirubin", "instances": 71, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 65, "metric_value": 0.0, "depth": 8}
                        if obj[5]>11:
                           return 'liver'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=17.273482007808447:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=78:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>31:
                           return 'liver'
                        elif obj[5]<=31:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>78:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Protiens", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=76:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]>35:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>31:
                           return 'liver'
                        elif obj[5]<=31:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=35:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>5:
                           return 'liver'
                        elif obj[1]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>76:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[4]>29:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=231:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=21:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>21:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>231:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=29:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[6]>71:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=24:
                           return 'liver'
                        elif obj[5]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=71:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
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
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 4}
            if obj[6]>66:
               # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[5]>24:
                  # {"feature": "Alkaline_Phosphotase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=42:
                           return 'liver'
                        elif obj[4]>42:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'normal'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=28:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=24:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=66:
               # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[4]>15:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[5]>26:
                     return 'liver'
                  elif obj[5]<=26:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=15:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=6:
                     return 'normal'
                  elif obj[1]>6:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 70, "metric_value": -0.0, "depth": 4}
            if obj[6]>19.155279749709432:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 37, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=90.47138560532954:
                     # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=12:
                        # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>12:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]>7:
                           return 'liver'
                        elif obj[2]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>90.47138560532954:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>51:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=51:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]>27:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=40:
                           return 'normal'
                        elif obj[5]>40:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=27:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>18:
                           return 'liver'
                        elif obj[5]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=19.155279749709432:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[8]<=1:
                  # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
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
               elif obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 4}
            if obj[2]>3:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[8]>6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=88:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[6]>56:
                        return 'liver'
                     elif obj[6]<=56:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>23:
                           return 'normal'
                        elif obj[1]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[5]>88:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=6:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>68:
                        return 'liver'
                     elif obj[1]<=68:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=15:
                        return 'normal'
                     elif obj[1]>15:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[2]<=3:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=8:
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
   else:
      return 'liver'
