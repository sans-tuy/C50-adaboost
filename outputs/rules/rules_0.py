def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Alkaline_Phosphotase", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[3]<=291.0539499036609:
      # {"feature": "Age", "instances": 384, "metric_value": -0.0, "depth": 2}
      if obj[0]>44.583333333333336:
         # {"feature": "Albumin", "instances": 198, "metric_value": -0.0, "depth": 3}
         if obj[7]>26.2979797979798:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[8]<=22.914529914529915:
               # {"feature": "Total_Bilirubin", "instances": 101, "metric_value": -0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 92, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=38.30434782608695:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 64, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=29.078125:
                        # {"feature": "Total_Protiens", "instances": 42, "metric_value": 0.0, "depth": 8}
                        if obj[6]>63.92857142857143:
                           return 'liver'
                        elif obj[6]<=63.92857142857143:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>29.078125:
                        # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=27:
                           return 'liver'
                        elif obj[2]>27:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>38.30434782608695:
                     # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=13:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[5]>52:
                           return 'liver'
                        elif obj[5]<=52:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>13:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=1:
                  # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>20:
                           return 'normal'
                        elif obj[5]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>28:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>4:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>22.914529914529915:
               # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[2]<=4:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=52:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>52:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>4:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]>11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        return 'liver'
                     elif obj[4]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>13:
                        return 'normal'
                     elif obj[4]<=13:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[7]<=26.2979797979798:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>23.646973828484313:
               # {"feature": "Alamine_Aminotransferase", "instances": 64, "metric_value": 0.0, "depth": 5}
               if obj[4]<=38.71875:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 42, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=37.0:
                     # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=42:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>42:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>37.0:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[2]>9:
                           return 'liver'
                        elif obj[2]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
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
                     return 'liver'
               elif obj[4]>38.71875:
                  # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]>42:
                           return 'liver'
                        elif obj[5]<=42:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]<=23.646973828484313:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[1]>8:
                     return 'liver'
                  elif obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>26:
                           return 'normal'
                        elif obj[4]<=26:
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
      elif obj[0]<=44.583333333333336:
         # {"feature": "Albumin", "instances": 186, "metric_value": -0.0, "depth": 3}
         if obj[7]>27.349462365591396:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 108, "metric_value": -0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Aspartate_Aminotransferase", "instances": 86, "metric_value": -0.0, "depth": 5}
               if obj[5]<=120.22093023255815:
                  # {"feature": "Total_Protiens", "instances": 72, "metric_value": -0.0, "depth": 6}
                  if obj[6]>62.55555555555556:
                     # {"feature": "Total_Bilirubin", "instances": 56, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 48, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=31.229166666666668:
                           return 'normal'
                        elif obj[4]>31.229166666666668:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>17:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=62.55555555555556:
                     # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
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
               elif obj[5]>120.22093023255815:
                  # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=71:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>97:
                           return 'liver'
                        elif obj[4]<=97:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=80:
                           return 'liver'
                        elif obj[4]>80:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>71:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[1]<=33:
                  # {"feature": "Total_Protiens", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[6]>68:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>36:
                           return 'normal'
                        elif obj[5]<=36:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=26:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[6]<=68:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>30:
                           return 'liver'
                        elif obj[5]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>33:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[7]<=27.349462365591396:
            # {"feature": "Direct_Bilirubin", "instances": 78, "metric_value": -0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Total_Bilirubin", "instances": 65, "metric_value": 0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Total_Protiens", "instances": 64, "metric_value": 0.0, "depth": 6}
                  if obj[6]>44.734375:
                     # {"feature": "Alamine_Aminotransferase", "instances": 43, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=47.116279069767444:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=48.93103448275862:
                           return 'liver'
                        elif obj[5]>48.93103448275862:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>47.116279069767444:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=168:
                           return 'liver'
                        elif obj[5]>168:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=44.734375:
                     # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[4]>27:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=62:
                           return 'liver'
                        elif obj[5]>62:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=27:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        elif obj[8]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=1:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[1]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=23:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=17:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>7:
                           return 'normal'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>17:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>23:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=41:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>6:
                           return 'normal'
                        elif obj[6]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>41:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=55:
                           return 'liver'
                        elif obj[6]>55:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]<=2:
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
      # {"feature": "Albumin", "instances": 135, "metric_value": -0.0, "depth": 2}
      if obj[7]>25.214814814814815:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 79, "metric_value": -0.0, "depth": 3}
         if obj[8]<=15.329113924050633:
            # {"feature": "Age", "instances": 69, "metric_value": -0.0, "depth": 4}
            if obj[0]>39.608695652173914:
               # {"feature": "Alamine_Aminotransferase", "instances": 36, "metric_value": 0.0, "depth": 5}
               if obj[4]<=122.66666666666667:
                  # {"feature": "Total_Protiens", "instances": 26, "metric_value": -0.0, "depth": 6}
                  if obj[6]>61:
                     # {"feature": "Direct_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=12:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=14:
                           return 'liver'
                        elif obj[1]>14:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=61:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>122.66666666666667:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=39.608695652173914:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[1]<=24:
                  # {"feature": "Total_Protiens", "instances": 29, "metric_value": -0.0, "depth": 6}
                  if obj[6]>65:
                     # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=80:
                           return 'liver'
                        elif obj[5]>80:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'normal'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=65:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>24:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>15.329113924050633:
            return 'liver'
         else:
            return 'liver'
      elif obj[7]<=25.214814814814815:
         # {"feature": "Aspartate_Aminotransferase", "instances": 56, "metric_value": 0.0, "depth": 3}
         if obj[5]<=237.53571428571428:
            # {"feature": "Age", "instances": 45, "metric_value": 0.0, "depth": 4}
            if obj[0]>45.666666666666664:
               # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 5}
               if obj[1]>3:
                  # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[2]>11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]>46:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=7:
                           return 'liver'
                        elif obj[6]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=46:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=42:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[6]>51:
                           return 'liver'
                        elif obj[6]<=51:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>42:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=3:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=45.666666666666664:
               # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[1]>2:
                  # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=11:
                     # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>28:
                           return 'normal'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>11:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>38:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[8]>7:
                           return 'normal'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=38:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>59:
                           return 'normal'
                        elif obj[6]<=59:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=2:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[5]>237.53571428571428:
            # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": 0.0, "depth": 4}
            if obj[1]<=86:
               # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 5}
               if obj[2]<=4:
                  # {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[0]>46:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=181:
                        return 'normal'
                     elif obj[4]>181:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=46:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>4:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]>86:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
