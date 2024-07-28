#TABLE_STUDENT
import pandas as pd

ids = list(range(1, 21))
names = ["Ace", "Blaze", "Cash", "Duke", "Echo", "Frost", "Gage", "Hawk", "Jett", "Knox",
         "Luxe", "Mace", "Nova", "Onyx", "Pax", "Quill", "Rex", "Steel", "Talon", "Vex"]
student_df = pd.DataFrame({'ID': ids, 'Nama': names})
student_df.to_csv('student.csv', index=False)


#TABLE_LECTURER
data = {
    "ID": list(range(1, 61)),
    "nama": [
        "Adi Wijaya", "Budi Santoso", "Citra Ananda", "Dedi Setiawan", "Eka Rahmawati",
        "Feri Kurniawan", "Gita Permata", "Hariyanto Setiawan", "Indra Wijaya", "Joko Supriyadi",
        "Kiki Rahmawati", "Lina Kurniawati", "Maya Sari", "Nina Pratiwi", "Oki Susanto",
        "Putu Widi", "Qori Permata", "Rudi Santoso", "Santi Ananda", "Tari Pratiwi",
        "Umar Wirawan", "Vina Setiawati", "Wawan Kurniawan", "Xenia Rahma", "Yuli Andriani",
        "Zaki Permana", "Ayu Saraswati", "Beni Wirawan", "Cici Andriani", "Doni Pratama",
        "Endah Lestari", "Fani Susanto", "Gilang Purnama", "Hesti Permata", "Ilham Setiawan",
        "Junaedi Pratama", "Kirana Sari", "Lukman Wijaya", "Mira Kusuma", "Nadia Pratiwi",
        "Oni Susanto", "Pandu Wijaya", "Qori Setiawan", "Rina Kurniawati", "Susi Rahma",
        "Tomi Pratama", "Uli Purnama", "Vino Andri", "Widi Rahmawati", "Xander Pratama",
        "Yusuf Permana", "Zara Kusuma", "Agus Wijaya", "Bona Santoso", "Cici Ananda",
        "Dian Setiawan", "Edo Rahma", "Fika Pratama", "Gina Permata", "Heri Setiawan"
    ]
}
lecturer_df = pd.DataFrame(data)
lecturer_df.to_csv('lecturer.csv', index=False)