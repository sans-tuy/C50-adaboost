def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": -0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]<=81.47896483100102:
            # {"feature": "Alkaline_Phosphotase", "instances": 144, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 110, "metric_value": 0.0, "depth": 5}
               if obj[8]<=143.9669375902827:
                  # {"feature": "Alamine_Aminotransferase", "instances": 107, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=41.691588785046726:
                     # {"feature": "Total_Bilirubin", "instances": 75, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 45, "metric_value": -0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=4:
                           return 'liver'
                        elif obj[2]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>41.691588785046726:
                     # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=62.63863411043676:
                        # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=9:
                           return 'liver'
                        elif obj[2]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>62.63863411043676:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>143.9669375902827:
                  # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=20:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>20:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 34, "metric_value": -0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=83.17857142857143:
                     # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=32:
                        # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>32:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>83.17857142857143:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]>81.47896483100102:
            # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 4}
            if obj[1]<=7:
               # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[4]>18:
                  return 'liver'
               elif obj[4]<=18:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[1]>7:
               # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     return 'normal'
                  elif obj[8]<=1:
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
         # {"feature": "Total_Protiens", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[6]>47.559322033898304:
            # {"feature": "Alkaline_Phosphotase", "instances": 79, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 54, "metric_value": -0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 50, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=16:
                     # {"feature": "Alamine_Aminotransferase", "instances": 46, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=42.43478260869565:
                        # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=29:
                           return 'liver'
                        elif obj[2]>29:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>42.43478260869565:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=72:
                           return 'liver'
                        elif obj[2]>72:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>16:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>28:
                        return 'liver'
                     elif obj[5]<=28:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=1:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=13:
                           return 'normal'
                        elif obj[5]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=22:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 5}
               if obj[1]<=140.67416318740703:
                  # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=62:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=6:
                        return 'liver'
                     elif obj[8]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=28:
                           return 'liver'
                        elif obj[5]>28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]>62:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[5]>64:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=64:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>140.67416318740703:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=47.559322033898304:
            # {"feature": "Alkaline_Phosphotase", "instances": 39, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[8]<=13:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[5]>29:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=41:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>41:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=29:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[2]>5:
                           return 'liver'
                        elif obj[2]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>13:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>40:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=40:
                     return 'liver'
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
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Direct_Bilirubin", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Protiens", "instances": 81, "metric_value": -0.0, "depth": 6}
                  if obj[6]>61.160493827160494:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 61, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=87.60655737704919:
                        # {"feature": "Total_Bilirubin", "instances": 45, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>87.60655737704919:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[4]>56:
                           return 'liver'
                        elif obj[4]<=56:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=61.160493827160494:
                     # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[4]>14:
                        # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=14:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=31:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=32:
                           return 'liver'
                        elif obj[4]>32:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>31:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'liver'
                        elif obj[1]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=22:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Protiens", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[6]<=76:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[5]>30:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>29:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=29:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=17:
                           return 'liver'
                        elif obj[1]>17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=30:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]>76:
                  # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=26:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>2:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[2]<=6:
               # {"feature": "Alamine_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[4]<=87.6:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=21:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=67:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>67:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>21:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>87.6:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[6]>68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>80:
                        return 'liver'
                     elif obj[5]<=80:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=13:
                           return 'liver'
                        elif obj[1]>13:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=68:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
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
            elif obj[2]>6:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]>23:
                     return 'liver'
                  elif obj[1]<=23:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        return 'liver'
                     elif obj[4]<=28:
                        return 'normal'
                     else:
                        return 'normal'
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
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[6]<=69.21614882171913:
               # {"feature": "Direct_Bilirubin", "instances": 61, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": -0.0, "depth": 6}
                  if obj[8]>6:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=40.888888888888886:
                        # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>40.888888888888886:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]<=6:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=39:
                           return 'normal'
                        elif obj[5]>39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=46:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=65:
                        # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>65:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>74:
                           return 'liver'
                        elif obj[5]<=74:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]>46:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>69.21614882171913:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]>40:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[8]>3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=40:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>40:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=3:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=40:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=27:
                     return 'liver'
                  elif obj[5]>27:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]<=62:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 5}
               if obj[8]>6:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[2]>11:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>57:
                           return 'liver'
                        elif obj[5]<=57:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=6:
                  # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=27:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'normal'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>27:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'liver'
                     elif obj[4]<=25:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>62:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
