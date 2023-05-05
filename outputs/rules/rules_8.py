def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 233, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Age", "instances": 185, "metric_value": -0.0, "depth": 4}
            if obj[0]<=59.007173904132195:
               # {"feature": "Total_Protiens", "instances": 147, "metric_value": -0.0, "depth": 5}
               if obj[6]>59.14965986394558:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 107, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=282.7129912537788:
                     # {"feature": "Alamine_Aminotransferase", "instances": 103, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=41.10679611650485:
                        # {"feature": "Direct_Bilirubin", "instances": 75, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>41.10679611650485:
                        # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>282.7129912537788:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=59.14965986394558:
                  # {"feature": "Direct_Bilirubin", "instances": 40, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=11:
                        # {"feature": "Alamine_Aminotransferase", "instances": 26, "metric_value": -0.0, "depth": 8}
                        if obj[4]>23:
                           return 'liver'
                        elif obj[4]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>11:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>30:
                           return 'liver'
                        elif obj[4]<=30:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[4]>50:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]>22:
                           return 'liver'
                        elif obj[1]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=50:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]>59.007173904132195:
               # {"feature": "Aspartate_Aminotransferase", "instances": 38, "metric_value": 0.0, "depth": 5}
               if obj[5]<=77.07894736842105:
                  # {"feature": "Total_Protiens", "instances": 31, "metric_value": 0.0, "depth": 6}
                  if obj[6]>54:
                     # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=5:
                           return 'liver'
                        elif obj[2]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=54:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[4]>18:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=18:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>77.07894736842105:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=15:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>53:
                           return 'normal'
                        elif obj[4]<=53:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>15:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Age", "instances": 48, "metric_value": -0.0, "depth": 4}
            if obj[0]<=57.44569923452688:
               # {"feature": "Total_Protiens", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[6]>65.92307692307692:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]>30:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]>31:
                           return 'liver'
                        elif obj[4]<=31:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=30:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=30:
                           return 'liver'
                        elif obj[4]>30:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[5]>19:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[4]>29:
                           return 'liver'
                        elif obj[4]<=29:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=19:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=65.92307692307692:
                  # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]>24:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=24:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=16:
                           return 'normal'
                        elif obj[5]>16:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>9:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]>57.44569923452688:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 5}
               if obj[4]>16:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[5]>35:
                     return 'liver'
                  elif obj[5]<=35:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=16:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     return 'normal'
                  elif obj[1]<=1:
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
         # {"feature": "Age", "instances": 73, "metric_value": 0.0, "depth": 3}
         if obj[0]>4:
            # {"feature": "Alamine_Aminotransferase", "instances": 72, "metric_value": 0.0, "depth": 4}
            if obj[4]<=106.02777777777777:
               # {"feature": "Direct_Bilirubin", "instances": 51, "metric_value": -0.0, "depth": 5}
               if obj[2]<=39:
                  # {"feature": "Total_Bilirubin", "instances": 47, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=20.382978723404257:
                     # {"feature": "Total_Protiens", "instances": 33, "metric_value": 0.0, "depth": 7}
                     if obj[6]>53.31744211801017:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=52.96774193548387:
                           return 'liver'
                        elif obj[5]>52.96774193548387:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=53.31744211801017:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>20.382978723404257:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[5]>21:
                        # {"feature": "Total_Protiens", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[6]>7:
                           return 'liver'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>39:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[4]>106.02777777777777:
               # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[1]<=63:
                  # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=32:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=176:
                        # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=72:
                           return 'liver'
                        elif obj[6]>72:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>176:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>32:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>63:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]<=4:
            return 'normal'
         else:
            return 'normal'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Total_Protiens", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[6]>22.141963590857678:
         # {"feature": "Alkaline_Phosphotase", "instances": 163, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 115, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alamine_Aminotransferase", "instances": 106, "metric_value": 0.0, "depth": 5}
               if obj[4]<=45.632075471698116:
                  # {"feature": "Age", "instances": 77, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=48.5974025974026:
                     # {"feature": "Total_Bilirubin", "instances": 41, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=13:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=27.066666666666666:
                           return 'liver'
                        elif obj[5]>27.066666666666666:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]>48.5974025974026:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 36, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=39:
                           return 'liver'
                        elif obj[1]>39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]>45.632075471698116:
                  # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": -0.0, "depth": 6}
                  if obj[2]>3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[5]>65:
                        return 'liver'
                     elif obj[5]<=65:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]<=3:
                     # {"feature": "Age", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[0]<=29:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[0]>29:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>33:
                           return 'liver'
                        elif obj[5]<=33:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]<=25:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 6}
                  if obj[5]>19:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=19:
                     # {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[0]>60:
                        return 'liver'
                     elif obj[0]<=60:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]>25:
                  # {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[0]>26:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>24:
                        return 'normal'
                     elif obj[1]<=24:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=26:
                     return 'liver'
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
               if obj[0]<=49.1578947368421:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=76:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'liver'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>76:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[0]>49.1578947368421:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[1]>11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=88:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=5:
                           return 'liver'
                        elif obj[8]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>88:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=298:
                           return 'liver'
                        elif obj[5]>298:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=11:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>25:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'normal'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 50, "metric_value": -0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Age", "instances": 28, "metric_value": -0.0, "depth": 4}
            if obj[0]>48.642857142857146:
               # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
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
            elif obj[0]<=48.642857142857146:
               # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]>32:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=32:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
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
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>12:
                     return 'normal'
                  elif obj[1]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 4}
            if obj[4]>30:
               # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Age", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=65:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]>65:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>48:
                     # {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[0]>38:
                        return 'liver'
                     elif obj[0]<=38:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=48:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]<=30:
               # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[0]>33:
                           return 'liver'
                        elif obj[0]<=33:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=9:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[0]>4:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[0]<=4:
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
      else:
         return 'liver'
   else:
      return 'liver'
