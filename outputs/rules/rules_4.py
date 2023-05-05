def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Age", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[0]>43.12091503267974:
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": -0.0, "depth": 3}
         if obj[6]>60.564935064935064:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 119, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 91, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 67, "metric_value": 0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Total_Bilirubin", "instances": 66, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 8}
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
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
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
            elif obj[8]<=1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[5]<=73.14285714285714:
                  # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=33:
                     # {"feature": "Alkaline_Phosphotase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>33:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>73.14285714285714:
                  # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[4]>29:
                     return 'liver'
                  elif obj[4]<=29:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=60.564935064935064:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[8]<=96:
               # {"feature": "Alamine_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[4]<=44.58064516129032:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=54:
                     # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>54:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]>44.58064516129032:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=59:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>59:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>17:
                        return 'liver'
                     elif obj[1]<=17:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>96:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[0]<=43.12091503267974:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 115, "metric_value": 0.0, "depth": 4}
            if obj[8]<=68.6571116534237:
               # {"feature": "Direct_Bilirubin", "instances": 98, "metric_value": -0.0, "depth": 5}
               if obj[2]<=38.281630864571:
                  # {"feature": "Total_Protiens", "instances": 92, "metric_value": -0.0, "depth": 6}
                  if obj[6]>58.880434782608695:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 68, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=65.41176470588235:
                        # {"feature": "Total_Bilirubin", "instances": 56, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=18:
                           return 'liver'
                        elif obj[1]>18:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>65.41176470588235:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=37:
                           return 'liver'
                        elif obj[1]>37:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=58.880434782608695:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=18:
                           return 'liver'
                        elif obj[1]>18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>38.281630864571:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]>68.6571116534237:
               # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[4]>19:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[5]>62:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=62:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]>5:
                           return 'liver'
                        elif obj[2]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=19:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]>7:
               # {"feature": "Total_Protiens", "instances": 26, "metric_value": -0.0, "depth": 5}
               if obj[6]>67:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=57:
                           return 'normal'
                        elif obj[4]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=23:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=67:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=39:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]>47:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=47:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[8]<=7:
               # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=15:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=103:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>103:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        return 'liver'
                     elif obj[4]<=28:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
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
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[6]>21.50804221771271:
            # {"feature": "Alamine_Aminotransferase", "instances": 115, "metric_value": -0.0, "depth": 4}
            if obj[4]<=44.11304347826087:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 83, "metric_value": 0.0, "depth": 5}
               if obj[8]<=38.88134348379403:
                  # {"feature": "Age", "instances": 71, "metric_value": -0.0, "depth": 6}
                  if obj[0]<=50.140845070422536:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 37, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Total_Bilirubin", "instances": 36, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[0]>50.140845070422536:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 34, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=94.0963727722383:
                        # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=22:
                           return 'liver'
                        elif obj[1]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>94.0963727722383:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>38.88134348379403:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[5]>28:
                     # {"feature": "Age", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[0]>20:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[0]<=20:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=28:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Age", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[0]>27:
                           return 'liver'
                        elif obj[0]<=27:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[4]>44.11304347826087:
               # {"feature": "Aspartate_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[5]>25:
                  # {"feature": "Age", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[0]>35:
                     # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=33:
                        # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>33:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=35:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>8:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
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
               elif obj[5]<=25:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[6]<=21.50804221771271:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 36, "metric_value": 0.0, "depth": 4}
            if obj[8]<=9:
               # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[2]<=4:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[5]>21:
                     # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        # {"feature": "Age", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[0]<=49:
                           return 'liver'
                        elif obj[0]>49:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=21:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>4:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>13:
                     # {"feature": "Age", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[0]>33:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[0]<=33:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>9:
               # {"feature": "Age", "instances": 5, "metric_value": -0.0, "depth": 5}
               if obj[0]>48:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[0]<=48:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
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
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Direct_Bilirubin", "instances": 62, "metric_value": 0.0, "depth": 3}
         if obj[2]<=29.629032258064516:
            # {"feature": "Total_Bilirubin", "instances": 43, "metric_value": -0.0, "depth": 4}
            if obj[1]<=26.069767441860463:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 30, "metric_value": -0.0, "depth": 5}
               if obj[8]<=37:
                  # {"feature": "Total_Protiens", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[6]>45:
                     # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[4]>20:
                        # {"feature": "Age", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[0]<=44:
                           return 'liver'
                        elif obj[0]>44:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=20:
                        # {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[0]>13:
                           return 'liver'
                        elif obj[0]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=45:
                     # {"feature": "Age", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[0]>33:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>42:
                           return 'liver'
                        elif obj[4]<=42:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[0]<=33:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>37:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]>26.069767441860463:
               # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[4]<=142:
                  return 'liver'
               elif obj[4]>142:
                  # {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=50:
                     return 'normal'
                  elif obj[0]>50:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[2]>29.629032258064516:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 4}
            if obj[8]>5:
               # {"feature": "Age", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[0]<=50:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=52:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>47:
                           return 'liver'
                        elif obj[5]<=47:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>52:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>18:
                        return 'normal'
                     elif obj[1]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[0]>50:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=5:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
