from api_key import *

class queryAPILinks():

    # api url/key object
    tmdbAPI = apiKeys()

    def getUpcomingMoviesLink(self):
        upcomingMoviesLink = "https://api.themoviedb.org/3/movie/upcoming" + self.tmdbAPI.getAPIKey() + "&language=en-US&page="
        return upcomingMoviesLink

    def getNowPlayingMoviesLink(self):
        nowPlayingMoviesLink = "https://api.themoviedb.org/3/movie/now_playing" + self.tmdbAPI.getAPIKey() + "&language=en-US&page="
        return nowPlayingMoviesLink

    def getPopularMoviesLink(self):
        popularMoviesLink = "https://api.themoviedb.org/3/movie/popular" + self.tmdbAPI.getAPIKey() + "&language=en-US&page="
        return popularMoviesLink

    def getTopRatedMoviesLink(self):
        topRatedMoviesLink = "https://api.themoviedb.org/3/movie/top_rated" + self.tmdbAPI.getAPIKey() + "&language=en-US&page="
        return topRatedMoviesLink

    def getTrendingMoviesTodayLink(self):
        trendingMoviesTodayLink = "https://api.themoviedb.org/3/trending/movie/day" + self.tmdbAPI.getAPIKey() 
        return trendingMoviesTodayLink

    def getTrendingMoviesWeeklyLink(self):
        trendingMoviesWeeklyLink = "https://api.themoviedb.org/3/trending/movie/week" + self.tmdbAPI.getAPIKey()
        return trendingMoviesWeeklyLink

    def getPopularTVShowsLink(self):
        popularTVShowsLink = "https://api.themoviedb.org/3/tv/popular" + self.tmdbAPI.getAPIKey() + "&language=en-US&page="
        return popularTVShowsLink

    def getTopRatedTVShowsLink(self):
        topRatedTVShowsLink = "https://api.themoviedb.org/3/tv/top_rated" + self.tmdbAPI.getAPIKey() + "&language=en-US&page="
        return topRatedTVShowsLink

    def getTrendingTVShowsTodayLink(self):
        trendingTVShowsTodayLink = "https://api.themoviedb.org/3/trending/tv/day" + self.tmdbAPI.getAPIKey()
        return trendingTVShowsTodayLink

    def getTrendingTVShowsWeeklyLink(self):
        trendingTVShowsWeeklyLink = "https://api.themoviedb.org/3/trending/tv/week" + self.tmdbAPI.getAPIKey()
        return trendingTVShowsWeeklyLink