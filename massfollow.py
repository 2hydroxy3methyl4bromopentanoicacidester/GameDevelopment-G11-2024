import requests, os

with open("massfollowids.txt", "r") as read:
    ids = [int(x.strip()) for x in read.readlines()]

FEDAUTH = "77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+MGUudHxhZGZzfDE0MjkyMDNAbGVhcm43NS5jYSwwZS50fGFkZnN8MTQyOTIwM0BsZWFybjc1LmNhLDEzMzc0MDE3MjQyMTg5MTEzOSxUcnVlLGVNT2ZVL2xES0w4RkdZL2dwWk1sOUxIZXN4ZnhZNmFha1ZpdXB6THdEMHE3MExjN01QQVRjK2pWUTl1NDladmNiVmtWMGNhd1dscE1wd1IyRVRsTGcyUm05ZTRCNVFTYUhZNUNuaWw2ZUhkMmIvWmsvUGJMbHIrTDBMSThxVzFvZWVMNFZtYUJtS2NjNFBJU2Vmc3c0Mlg5THRNWWk5YWUrZEVVekZUZEhKOWhxaS9MTW9ERkpwSnhuRVdCK0s5TGFEZTNacktpMjJ4dTJoQ3ZiQ2VaYmVvaDJuR0NraVZoTmluNDVBeEJIRmxKVzk1dGc1VFNWTEtBcnhaTndsL2hPQ1ZCc284K2VCMDdkdFlYVHo3anA5T1JTc1lDM2FMeWdQdUVkZ0NhU2xiZkoveEpHQ3lZeXlEanJGRUt3S1hnNmQ0WXYybDlOZEZVVktTVzArUVhxQT09LGh0dHBzOi8vcG9ydGFsLm1wc2QuY2EvPC9TUD4="
DIGEST = "0x239DE6EE96E70520155083E0C7B70F113760D35F6D8C6E24BAA530A79A544FD5FED8936E1D4D0B284ED470759986D6D8E39AB5C53726FBE140456E1ADFB7B58C,17 Oct 2024 20:22:32 -0000"
def FollowUser(id):
    id = str(id)
    return requests.post("https://portal.mpsd.ca/my/_vti_bin/client.svc/ProcessQuery",
                         headers={"Cookie": f"FedAuth={FEDAUTH};", "x-requestdigest":DIGEST},
                         data=f"""<Request xmlns="http://schemas.microsoft.com/sharepoint/clientquery/2009" SchemaVersion="15.0.0.0" LibraryVersion="16.0.0.0" ApplicationName="Javascript Library"><Actions><ObjectPath Id="1" ObjectPathId="0" /><Method Name="Follow" Id="2" ObjectPathId="0"><Parameters><Parameter Type="String">i:0e.t|adfs|{id}@learn75.ca</Parameter></Parameters></Method></Actions><ObjectPaths><Constructor Id="0" TypeId="{{cf560d69-0fdb-4489-a216-b6b47adf8ef8}}" /></ObjectPaths></Request>""")


print(FollowUser(2725844).status_code)