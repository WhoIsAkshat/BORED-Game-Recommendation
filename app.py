import streamlit as st
from streamlit_option_menu import option_menu
import requests
import pandas as pd
from bs4 import BeautifulSoup
import streamlit_authenticator as stauth
import database as db
import yaml
from pathlib import Path
from PIL import Image

st.set_page_config(
            page_title="BORED",
            page_icon="🕹",
            layout="wide"
        )

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo = current_dir / "assets" / "Asset 2.png"
logo = Image.open(logo)



col1, col2, col3 = st.columns(3)
with col2:
    st.image(logo, width=400)
    st.title(" ")

with st.sidebar:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col2:
        st.image(logo, width=200)
    st.text(" ")
    st.text(" ")
    selected_login = option_menu(
                menu_title=None,
                options=["Login", "Signup"],
                icons=["person", "list-task"],
                menu_icon="cast",
                default_index=0,
                styles={
                    "icon": {"color": "white", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#43454a",
                    },
                    "nav-link-selected": {"background-color": "grey"},
                },
            )

if selected_login == "Login":
    users = db.fetch_all_users()
    credentials = {
        'usernames': {
            item['key']: {
                'name': item['name'],
                'password': item['password']
            } for item in users
        }
    }

    cookie = {
        'expiry_days': 30,
        'key': 'abcdef$#@!',
        'name': 'game-recommend'
    }

    result = {
        'credentials': credentials,
        'cookie': cookie
    }

    yaml_data = yaml.dump(result, default_style='"', sort_keys=False)

    data_dict = yaml.safe_load(yaml_data)

    authenticator = stauth.Authenticate(
        data_dict['credentials'],
        data_dict['cookie']['name'],
        data_dict['cookie']['key'],
        data_dict['cookie']['expiry_days']
    )

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status is False:
        st.error("Username/password is incorrect")

    if authentication_status is None:
        st.warning("Please enter your username and password")

    if authentication_status:
        with st.sidebar:

            selected = option_menu(
                        menu_title=None,
                        options=["Homepage", "Search Game", "About Us", "Logout"],
                        icons=["house", "search", "person", "cast"],
                        menu_icon="cast",
                        default_index=0,
                        styles={
                            "icon": {"color": "white", "font-size": "25px"},
                            "nav-link": {
                                "font-size": "25px",
                                "text-align": "left",
                                "margin": "0px",
                                "--hover-color": "#43454a",
                            },
                            "nav-link-selected": {"background-color": "grey"},
                        },
                    )

        if selected == "Homepage":
            def fetch_poster(game_name):
                query = f"igdb {game_name}"  # the search query you want to make
                query.lower()  # make the search query lowercase
                query.replace("'", "%27")
                query.replace(" ", "+")
                url = f"https://www.google.com/search?q={query}&sxsrf=APwXEdf3TLg-HrIw4eQ83Fg608bhLjNKqA:1681742175435&source=lnms&tbm=isch&sa=X&ved=2ahUKEwisuuHnkbH-AhXYs6QKHYg2AKwQ_AUoAXoECAEQAw&biw=2304&bih=1130&dpr=0.83"  # the URL of the search result page

                response = requests.get(url)  # make a GET request to the URL
                soup = BeautifulSoup(response.text, "html.parser")  # parse the HTML content with BeautifulSoup

                img_tag = soup.find("img", {"class": "yWs4tf"})

                if img_tag is not None:
                    img_link = img_tag.get("src")
                    return img_link  # print the first image link

            games = pd.read_pickle(open('game_list.pkl', 'rb'))

            st.title(f"Welcome, {name}")
            st.title(" ")

            st.header("Trending Games")
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                g1 = "Dead islands 2"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c2:
                g1 = "Hogwarts Legacy"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c3:
                g1 = "Genshin Impact"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c4:
                g1 = "Dead Space"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c5:
                g1 = "FIFA 23"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)

            st.title(" ")

            st.header("Top Action Games")
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                g1 = "The Last of Us Part-I"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c2:
                g1 = "Assassin's Creed Valhalla"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c3:
                g1 = "Shadow of the Tomb Raider"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c4:
                g1 = "Returnal"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c5:
                g1 = "Resident Evil 4"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)

            st.title(" ")

            st.header("Top Sports Games")
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                g1 = "NBA 2K23"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c2:
                g1 = "Madden NFL 23"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c3:
                g1 = "Forza"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c4:
                g1 = "EA Sports PGA Tour"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c5:
                g1 = "FIFA 23"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)

            st.title(" ")

            st.header("Top Horror Games")
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                g1 = "Death Stranding: Director's Cut"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c2:
                g1 = "Until Dawn"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c3:
                g1 = "Prey"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c4:
                g1 = "Alien Isolation"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)
            with c5:
                g1 = "Ghost of Tsushima"
                st.subheader(g1)
                st.image(fetch_poster(g1), width=240)

            # ----HIDE-STREAMLIT-STYLE----
            hide_st_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_st_style, unsafe_allow_html=True)

        if selected == "Search Game":

            def fetch_poster(game_name):
                query = f"igdb {game_name}"  # the search query you want to make
                query.lower()  # make the search query lowercase
                query.replace("'", "%27")
                query.replace(" ", "+")
                url = f"https://www.google.com/search?q={query}&sxsrf=APwXEdf3TLg-HrIw4eQ83Fg608bhLjNKqA:1681742175435&source=lnms&tbm=isch&sa=X&ved=2ahUKEwisuuHnkbH-AhXYs6QKHYg2AKwQ_AUoAXoECAEQAw&biw=2304&bih=1130&dpr=0.83"  # the URL of the search result page

                response = requests.get(url)  # make a GET request to the URL
                soup = BeautifulSoup(response.text, "html.parser")  # parse the HTML content with BeautifulSoup

                img_tag = soup.find("img", {"class": "yWs4tf"})

                if img_tag is not None:
                    img_link = img_tag.get("src")
                    return img_link  # print the first image link


            def recommend(game):
                game_idx = int(games[games['name'] == game].new_index) - 1
                distances = sorted(list(enumerate(similarity[game_idx])), reverse=True, key=lambda x: x[1])[1:6]
                recommended_game_names = []
                recommended_game_posters = []
                for i in distances:
                    recommended_game_posters.append(fetch_poster(games.name[i[0]]))
                    recommended_game_names.append(games.name[i[0]])

                return recommended_game_names, recommended_game_posters


            games = pd.read_pickle(open('game_list.pkl', 'rb'))
            similarity = pd.read_pickle(open('similarity.pkl', 'rb'))
            game_desc = pd.read_pickle(open('game_desc.pkl', 'rb'))

            st.title('Search a Recommendation')

            game_list = games['name'].values
            selected_game = st.selectbox(
                "Type or select a game from the dropdown",
                game_list
            )

            col1, col2 = st.columns(2)
            with col1:
                st.image(fetch_poster(selected_game), width=600)
            with col2:
                st.title(selected_game)
                idx = int(games[games['name'] == selected_game].new_index) - 1
                st.subheader(game_desc.publisher[idx])
                st.subheader(game_desc.genre[idx])
                st.subheader(game_desc.original_price[idx])
                st.header('About')
                st.markdown(game_desc.game_description[idx], unsafe_allow_html=False)

            if st.button('Recommend:'):
                recommended_game_names, recommended_game_posters = recommend(
                    selected_game)
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    st.header(recommended_game_names[0])
                    st.image(recommended_game_posters[0], width=240)
                with col2:
                    st.header(recommended_game_names[1])
                    st.image(recommended_game_posters[1], width=240)
                with col3:
                    st.header(recommended_game_names[2])
                    st.image(recommended_game_posters[2], width=240)
                with col4:
                    st.header(recommended_game_names[3])
                    st.image(recommended_game_posters[3], width=240)
                with col5:
                    st.header(recommended_game_names[4])
                    st.image(recommended_game_posters[4], width=240)

        if selected == "About Us":
            col1, col2, col3 = st.columns(3)
            with col2:
                st.title("Team ARES III")
                st.text(" ")
            mem1 = current_dir / "assets" / "akshat.png"
            mem1 = Image.open(mem1)
            mem2 = current_dir / "assets" / "ishani.png"
            mem2 = Image.open(mem2)
            mem3 = current_dir / "assets" / "tanya.png"
            mem3 = Image.open(mem3)
            mem4 = current_dir / "assets" / "smriti.png"
            mem4 = Image.open(mem4)
            ww = 250
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.image(mem1,width=ww)
            with c2:
                st.header("Akshat Garg")
                st.subheader("Every pizza, is a personal Pizza🍕. Thank You")
            with c3:
                st.image(mem2,width=ww)
            with c4:
                st.header("Ishani Bhatia")
                st.subheader("I code in Ook!🐽")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.image(mem3,width=ww)
            with c2:
                st.header("Tanya Chopra")
                st.subheader("Why to deal with anything in a logical way"
                             "when u have the option of absolutely losing ur mind 🤯")
            with c3:
                st.image(mem4,width=ww)
            with c4:
                st.header("Smriti")
                st.subheader("I won’t be impressed with technology until "
                             "I can download food🍔🍟🌭🍕")

        if selected == "Logout":
            st.title("Did you get 'bored' of BORED ?? ")
            authenticator.logout("Logout")

if selected_login == "Signup":
    st.title("Create an Account")
    new_name = st.text_input('Name')
    new_user = st.text_input('Username')
    new_pass = st.text_input('Password')

    hashed_password = stauth.Hasher([new_pass]).generate()

    if st.button('SignUp'):
        db.insert_user(new_user, new_name, hashed_password[0])
        st.success("You have successfully created an account. Go to the Login Menu to login.")