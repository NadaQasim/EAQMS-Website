class AQI:
    def calculate_aqi(Cp, Ih, Il, BPh, BPl):
        """
        Function to calculate AQI
        Cp : Concentration of particulate matter (PM10)
        Ih : AQI High
        Il : AQI Low
        BPh : Breakpoint High
        BPl : Breakpoint Low
        """

        aqi = ((Ih - Il) / (BPh - BPl)) * (Cp - BPl) + Il
        aqi = round(aqi)
        return aqi

    @staticmethod
    def get_aqi_pm(pm_val):

        if pm_val > 605:
            return AQI.calculate_aqi(pm_val, 500, 401, 604, 505)
        elif pm_val > 505:
            return AQI.calculate_aqi(pm_val, 500, 401, 604, 505)
        elif pm_val > 425:
            return AQI.calculate_aqi(pm_val, 400, 301, 504, 425)
        elif pm_val > 355:
            return AQI.calculate_aqi(pm_val, 300, 201, 424, 355)
        elif pm_val > 255:
            return AQI.calculate_aqi(pm_val, 200, 151, 354, 255)
        elif pm_val > 155:
            return AQI.calculate_aqi(pm_val, 150, 101, 254, 155)
        elif pm_val > 55:
            return AQI.calculate_aqi(pm_val, 100, 51, 154, 55)
        else:
            return AQI.calculate_aqi(pm_val, 50, 0, 54, 0)

    @staticmethod
    def get_aqi_pm2_5(pm_val):
        """
        Function to calculate AQI for PM2.5
        pm_val: The measured PM2.5
        """
        if pm_val > 251:
            return AQI.calculate_aqi(pm_val, 500, 401, 350.4, 251)
        elif pm_val > 121:
            return AQI.calculate_aqi(pm_val, 400, 301, 250, 121)
        elif pm_val > 91:
            return AQI.calculate_aqi(pm_val, 300,201, 120, 91)
        elif pm_val > 61:
            return AQI.calculate_aqi(pm_val, 200, 101, 90, 61)
        elif pm_val > 31:
            return AQI.calculate_aqi(pm_val, 100, 51, 60, 31)
        else:
            return AQI.calculate_aqi(pm_val, 50, 0, 30, 0)

    @staticmethod
    def get_final_aqi(pm10_val, pm2_5_val):
        """
        Function to calculate the final AQI (the maximum of PM10 and PM2.5 AQIs)
        pm10_val: The measured PM10
        pm2_5_val: The measured PM2.5
        """
        aqi_pm10 = AQI.get_aqi_pm(pm10_val)
        aqi_pm2_5 = AQI.get_aqi_pm2_5(pm2_5_val)
        full_info = []

        if aqi_pm10 > aqi_pm2_5:
            final_aqi = aqi_pm10
        else:
            final_aqi = aqi_pm2_5

        full_info.append(final_aqi)
        if final_aqi <= 50:
            full_info.append("Good")
            full_info.append("#2ec059")
        elif final_aqi > 50 and final_aqi <= 100:
            full_info.append("Moderate")
            full_info.append("#f1e25e")
        elif final_aqi > 100 and final_aqi <= 150:
            full_info.append("Unhealthy(S)")
            full_info.append("#ff773f")
        elif final_aqi > 150 and final_aqi <= 200:
            full_info.append("Unhealthy")
            full_info.append("#ff4848")
        elif final_aqi > 200 and final_aqi <= 300:
            full_info.append("Very Unhealthy")
            full_info.append("#bd51f1")
        elif final_aqi > 300 and final_aqi <= 500:
            full_info.append("Hazardous")
            full_info.append("#da4d77")
        elif final_aqi > 500:
            full_info.append("Hazardous")
            full_info.append("#7E0023")

        return full_info

