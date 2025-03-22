from flask import Blueprint, render_template

bp = Blueprint("notice", __name__, template_folder="../templates/notice")

@bp.route("/")
def notice_list():
    notices = [
        {"id": 1, "title": "첫 번째 공지사항", "content": "공지사항 내용 1"},
        {"id": 2, "title": "두 번째 공지사항", "content": "공지사항 내용 2"},
    ]
    return render_template("notice/list.html", notices=notices)

@bp.route("/<int:notice_id>")
def notice_detail(notice_id):
    return render_template("notice/detail.html", notice_id=notice_id)