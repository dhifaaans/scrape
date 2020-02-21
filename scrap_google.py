{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Agar Tak Kelamaan di Dapur Saat Masak, Lakukan 10 Trik ...', 'link': 'https://food.detik.com/info-kuliner/d-4482407/agar-tak-kelamaan-di-dapur-saat-masak-lakukan-10-trik-praktis-ini'}, {'title': 'Biar Masak Tak Kelamaan di Dapur, Lakukan 6 Trik Ini', 'link': 'https://food.detik.com/info-kuliner/d-3677442/biar-masak-tak-kelamaan-di-dapur-lakukan-6-trik-ini'}, {'title': 'Kumpulan Tips Dapur dan Cara Memasak - Sasa', 'link': 'http://www.kreasisasa.com/cookingnary'}, {'title': '3.982 resep dapur enak dan sederhana - Cookpad', 'link': 'https://cookpad.com/id/cari/dapur'}, {'title': '9 Trik Dapur Terbaru yang Bikin Masak Jadi Lebih Mudah ...', 'link': 'https://www.idntimes.com/food/recipe/andry-trisandy/9-trik-dapur-terbaru-yang-bikin-masak-jadi-lebih-mudah-1'}, {'title': '5 Tips Agar Dapur Tetap Rapi Selama Memasak | ResepKoki', 'link': 'https://resepkoki.id/5-tips-memasak-di-dapur-lebih-rapi/'}, {'title': '7 Tips Aman Dan Nyaman Memasak Makanan Didapur', 'link': 'http://suksesjayamlg.com/dnews/140004/7-tips-aman-dan-nyaman-memasak-makanan-didapur.html'}, {'title': 'Hanya Ada Waktu 15 Menit di Dapur? Resep Masakan Praktis ...', 'link': 'https://bp-guide.id/AX6sdmiH'}]\n"
     ]
    }
   ],
   "source": [
    "import urllib\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# desktop user-agent\n",
    "USER_AGENT = \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0\"\n",
    "# mobile user-agent\n",
    "MOBILE_USER_AGENT = \"Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36\"\n",
    "\n",
    "query = \"cara memasak di dapur\"\n",
    "query = query.replace(' ', '+')\n",
    "URL = f\"https://google.com/search?q={query}\"\n",
    "\n",
    "headers = {\"user-agent\": USER_AGENT}\n",
    "resp = requests.get(URL, headers=headers)\n",
    "\n",
    "if resp.status_code == 200:\n",
    "    soup = BeautifulSoup(resp.content, \"html.parser\")\n",
    "    results = []\n",
    "    for g in soup.find_all('div', class_='r'):\n",
    "        anchors = g.find_all('a')\n",
    "        if anchors:\n",
    "            link = anchors[0]['href']\n",
    "            \n",
    "            title = g.find('h3').text\n",
    "            item = {\n",
    "                \"title\": title,\n",
    "                \"link\": link\n",
    "            }\n",
    "            results.append(item)\n",
    "    print(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
