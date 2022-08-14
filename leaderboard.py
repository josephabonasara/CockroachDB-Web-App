from models import Score


class Leaderboard:
    def get_scores(self):
        return self.prepare_scores()


    def prepare_scores(self):
        scores = []
        scores.append(Score(1, 8, "Marlene F. Martell", 1298))
        scores.append(Score(2, 1, "Curtis D. Torres", 800))
        scores.append(Score(3, 7, "Sandy D. Martinez", 765))
        scores.append(Score(4, 3, "James O. Ewing", 721))

        scores.sort(reverse=True, key=lambda e: e.points)

        result = list(map(lambda score, i: {'id': score.id,
                                            'ranking': i + 1,
                                            'avatar': self.get_avatar_dic(),
                                            'playername': score.playername,
                                            'points': score.points
                                            },
                        scores,
                        list(range(len(scores)))))

        return result

    def get_avatar_dic(self):
        return {
        "0":"not set",
        "1":"👨🏻",
        "2":"👨🏼",
        "3":"👨🏽",
        "4":"👨🏾",
        "5":"👨🏿",
        "6":"👩🏻",
        "7":"👩🏼",
        "8":"👩🏽",
        "9":"👩🏾",
        "10":"👩🏿"
        }