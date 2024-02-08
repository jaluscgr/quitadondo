import flet as ft


def main(page):
    class AdaptiveIconButton(ft.IconButton):
        def __init__(self, ios_icon, android_icon):
            super().__init__()
            self._ios_icon = ios_icon
            self._android_icon = android_icon

        def on_update(self):
            self.icon = (
                self._ios_icon
                if self.page.platform == ft.PagePlatform.IOS
                or self.page.platform == ft.PagePlatform.MACOS
                else self._android_icon
            )

    def set_android(e):
        page.platform = ft.PagePlatform.ANDROID
        page.update()
        print("New platform:", page.platform)

    def set_ios(e):
        page.platform = "ios"
        page.update()
        print("New platform:", page.platform)

    add_icon = AdaptiveIconButton(
        ios_icon=ft.icons.ABC, android_icon=ft.icons.ADD
    )
    page.add(add_icon)
    page.adaptive = True

    page.add(
        ft.Switch(label="Switch A", adaptive=True),
        ft.ElevatedButton(
            "Set Android", on_click=set_android, content=ft.Text("Set Android")
        ),
        ft.ElevatedButton("Set iOS", on_click=set_ios, content=ft.Text("Set iOS")),
    )

    print("Default platform:", page.platform)


ft.app(target=main)